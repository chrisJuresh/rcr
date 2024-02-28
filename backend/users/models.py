from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Role(models.Model):
    """
    Defines various roles available in the system.
    """
    class RoleChoices(models.TextChoices):
        REVIEWER = 'REVIEWER', 'Reviewer'
        REPRESENTATIVE = 'REPRESENTATIVE', 'Representative'
        TRUST_EMPLOYEE = 'TRUST_EMPLOYEE', 'Trust Employee'
        RCR_EMPLOYEE = 'RCR_EMPLOYEE', 'RCR Employee'

    name = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        unique=True,
        verbose_name='Role Name'
    )

    def __str__(self):
        return self.get_name_display()

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    """
    Custom user model that extends AbstractUser with roles and titles.
    """
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
        null=True,
        max_length=4,
        blank=True,
        verbose_name='Title'
    )

class UserRole(models.Model):
    """
    Intermediate model to represent the many-to-many relationship between Users and Roles.
    """
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
    approved = models.BooleanField(
        default=False,
        verbose_name='Approved'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'role'], name='unique_user_role')
        ]
        verbose_name = 'User Role'
        verbose_name_plural = 'User Roles'

    def __str__(self):
        return f"{self.user.username}'s role as {self.role}"

class ReviewerInfo(models.Model):
    """
    Additional information for users with the Reviewer role.
    """
    user_role = models.OneToOneField(
        UserRole,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='User Role',
        limit_choices_to={'role__name': Role.RoleChoices.REVIEWER}
    )

    def __str__(self):
        return f"{self.user_role.user.username}'s reviewer info"

class RepresentativeInfo(models.Model):
    """
    Additional information for users with the Representative role.
    """
    user_role = models.OneToOneField(
        UserRole,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name='User Role',
        limit_choices_to={'role__name': Role.RoleChoices.REPRESENTATIVE}
    )

    def __str__(self):
        return f"{self.user_role.user.username}'s representative info"
