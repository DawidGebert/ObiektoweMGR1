from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
# Create your models here.

class UserManager(BaseUserManager):
    def createUser(self, username,email,password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a email')
        
        user=self.model(username=username,email=self._normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def createSuperuser(self, username,email,password=None):
        if password is None:
            raise TypeError('Password should not be None')
        
        user=self.createUser(username,email,password)
        user.is_superuser = True
        user.save()
        return user
    

