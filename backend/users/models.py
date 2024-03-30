from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from trusts.models import Trust
from django.dispatch import receiver
from roles.models import Role
from specialities.models import ConsultantType, Speciality

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import Permission
import logging

class UnauthenticatedUser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=128)
    token = models.CharField(max_length=255)       

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email Address')

    objects = UserManager()  
    
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  
    
    roles = models.ManyToManyField(
        Role,
        through='UserRole',
        blank=True,
        related_name='users',
        verbose_name='User Roles'
    )
    title = models.CharField(
        max_length=4,
        blank=True,
        verbose_name='Title'
    )
    trust = models.ForeignKey(
        Trust, 
        on_delete=models.CASCADE, 
        null=True,
        blank=True, 
        verbose_name='Trust'
    )
    trust_approved = models.BooleanField(
        default=False,
        verbose_name='Trust Approved'
    )
    
class UserRole(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_roles',
        verbose_name='User'
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='role_users',
        verbose_name='Role'
    )
    requested = models.BooleanField(
        default=False,
        verbose_name='Role Requested'
    )
    approved = models.BooleanField(
        default=False,
        verbose_name='Role Approved'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'role'], name='unique_user_role')
        ]
        verbose_name = 'User Role'
        verbose_name_plural = 'User Roles'

    def __str__(self):
        return f"{self.user.email}'s role as {self.role}"

class Reviewer(models.Model):
    user_role = models.OneToOneField(
        UserRole,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='User Role',
        limit_choices_to={'role__name': Role.RoleChoices.REVIEWER}
    )

    consultant_type = models.ManyToManyField(ConsultantType, blank=True)

    def __str__(self):
        return f"{self.user_role.user.email}'s reviewer info"

class Representative(models.Model):
    user_role = models.OneToOneField(
        UserRole,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='User Role',
        limit_choices_to={'role__name': Role.RoleChoices.REPRESENTATIVE}
    )

    specialities = models.ManyToManyField(Speciality, blank=True)

    def __str__(self):
        return f"{self.user_role.user.email}'s representative info"

logger = logging.getLogger(__name__)

ROLE_PERMISSION_MAPPING = {
    Role.RoleChoices.RCR_EMPLOYEE: 'can_rcr_review_jdprocess',
    Role.RoleChoices.REVIEWER: 'can_rsa_review_jdprocess',
    Role.RoleChoices.TRUST_EMPLOYEE: 'add_jdprocess'
}

def manage_user_permission(user, codename, add_permission=True):
    try:
        permission = Permission.objects.get(content_type__app_label='jds', codename=codename)
        if add_permission:
            user.user_permissions.add(permission)
        else:
            user.user_permissions.remove(permission)
        user.save()
    except Permission.DoesNotExist:
        logger.error(f"Permission '{codename}' not found. Ensure you have the correct codename and app label.")

@receiver(post_save, sender=UserRole)
def update_permissions(sender, instance, **kwargs):
    codename = ROLE_PERMISSION_MAPPING.get(instance.role.name)
    if codename:
        manage_user_permission(instance.user, codename, add_permission=instance.approved)

@receiver(post_delete, sender=UserRole)
def cleanup_permissions(sender, instance, **kwargs):
    codename = ROLE_PERMISSION_MAPPING.get(instance.role.name)
    if codename:
        manage_user_permission(instance.user, codename, add_permission=False)
