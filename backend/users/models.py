from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from trusts.models import Trust
from roles.models import Role
from specialities.models import ConsultantType, Speciality
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import Permission

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

    title = models.CharField(
        max_length=4,
        blank=True,
    )

    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

class UserTrust(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_trusts',
    )
    trust = models.ForeignKey(
        Trust,
        on_delete=models.CASCADE,
    )
    requested = models.BooleanField(
        default=False,
    )
    approved = models.BooleanField(
        default=False,
    )
    comments = models.TextField(
        blank=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'trust'], name='unique_user_trust')
        ]

    def __str__(self):
        return f"{self.user.email}'s association with {self.trust.name}"

class UserSpecialities(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_specialities',
    )

    consultant_type = models.ForeignKey(ConsultantType, blank=True, null=True, on_delete=models.SET_NULL)
    specialities = models.ManyToManyField(Speciality, blank=True)

    def __str__(self):
        return f"{self.user.email}'s Specialities"

class UserRole(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_roles',
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
    )
    requested = models.BooleanField(
        default=False,
    )
    approved = models.BooleanField(
        default=False,
    )
 
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'role'], name='unique_user_role')
        ]

    def __str__(self):
        return f"{self.user.email}'s role as {self.role}"
