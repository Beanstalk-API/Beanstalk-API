from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name']

    def to_dict(self):
        return {
            'email': self.email,
            'name': self.name
        }

# Generated Code model
class Code(models.Model):
    model_name = models.CharField(max_length=255)
    framework = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    backend = models.TextField(max_length=255)
    code = models.TextField()

    def to_dict(self):
        return {
            'language': self.language,
            'code': self.code,
        }