from django.db import models
from django.contrib.auth.models import User    # basic User model


# Create your models here.
class UserProfileInfo(models.Model):

    # Create relationship with builtin User model
    user = models.OneToOneField(User)

    # Add any additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User
        return self.user.username
