from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Signal receiver that listens for a User instance being saved.
@receiver(post_save, sender=User)
def build_profile(sender, instance, created, **kwargs):
    # If a new User instance is created, create a corresponding Profile instance.
    if created:
        Profile.objects.create(user=instance)

# Signal receiver that listens for a User instance being saved.
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # Save the Profile instance associated with the User instance.
    instance.profile.save()
