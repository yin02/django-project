from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# The Profile model is an extension of the default Django User model.
class Profile(models.Model):
    # One-to-one relationship between the User and Profile models.
    # When a User is deleted, their Profile is also deleted (CASCADE).
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The user's profile picture, with a default image and a specified upload directory.
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    # The user's location, stored as a string with a maximum length of 100 characters.
    location = models.CharField(max_length=100)

    # String representation of the Profile model, returning the associated User's username.
    def __str__(self):
        return self.user.username
