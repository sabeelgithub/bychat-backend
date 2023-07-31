from django.contrib.auth.models import AbstractUser,PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid





class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email,mobile, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email,mobile, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,mobile,password, **extra_fields)

    def create_superuser(self, email,mobile, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, mobile,password, **extra_fields)
        


class CustomUser(AbstractUser,PermissionsMixin):
    
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.IntegerField(unique=True)
    username = models.CharField(max_length=244,null=True)
    specification = models.CharField(max_length=50)
    is_otp_verified = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile','username']

    objects = CustomUserManager()

    
    
    def __str__(self):  
        return f'{self.username}' 
    




   
    
