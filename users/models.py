from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.role_name


class User(AbstractUser):
    pass
    contact_number = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def __str__(self):
        return self.username


