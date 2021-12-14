from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
        Custom user model
    """
    ROLE_CHOICES = (
        (0, 'employee'),
        (1, 'manager')
    )
    role = models.IntegerField(default=0, choices=ROLE_CHOICES)


