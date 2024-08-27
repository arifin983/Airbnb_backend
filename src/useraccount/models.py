
import uuid 

from django.conf import settings

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager


from django.db import models

class CustomUserManager(UserManager):
  
  def _create_user(self,name,email,password, **extra_fields):
    
    if not email:
      raise ValueError("The given email must be set")
    email = self.normalize_email(email)
    user = self.model(name=name, email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self.db)
    return user
  
  def create_user(self, name, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(name, email, password, **extra_fields)
  
  def create_superuser(self, name, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    
    if extra_fields.get('is_staff') is not True:
      raise ValueError("Superuser must have is_staff=True.")
    if extra_fields.get('is_superuser') is not True:
      raise ValueError("Superuser must have is_superuser=True.")
    
    return self._create_user(name, email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
  
  id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
  
  name = models.CharField(max_length=100 ,blank=True,null=True)
  
  email = models.EmailField(max_length=255, unique=True)
  
  avatar = models.ImageField(upload_to="uploads/avatars")
  
  is_staff = models.BooleanField(default=False)
  
  is_superuser = models.BooleanField(default=False)
  
  is_active = models.BooleanField(default=True)
  
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(blank=True,null=True)
  
  objects = CustomUserManager()
  
  USERNAME_FIELD = 'email'
  Email_Field= "email"
  REQUIRED_FIELDS = ["name",]
  
  def avatar_url(self):
        if self.avatar:
            return f'{settings.WEBSITE_URL}{self.avatar.url}'
        else:
            return ''

