from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(
        "City", on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return f'{self.user.username} Profile'


# once create new user, create new empty profile
@receiver(post_save, sender=User)  # => User model will be the sender
def create_user_profile(sender, instance, created, **kwargs):
    if created:  # => When a new instance of User created
        # => Instantiate a new Profile object and make its user field refers to that created User object.
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} '
