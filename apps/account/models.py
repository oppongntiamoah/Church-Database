from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(unique=True, max_length=50)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
        

    @property
    def is_staff(self):
        return self.is_admin


class Config(models.Model):
    church_name = models.CharField(max_length=250)
    sub_name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=250)
    branch_pastor = models.CharField(max_length=250)
    logo = models.ImageField(upload_to=None)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.church_name
    