from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def is_activation_key_expires(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOISES = (
        (MALE, 'M'),
        (FEMALE, 'F'),
    )

    user = models.OneToOneField(
        User,
        unique=True,
        null=False,
        db_index=True,
        on_delete=models.CASCADE
    )

    tagline = models.CharField(
        verbose_name='tags',
        max_length=128,
        blank=True
    )

    aboutme = models.TextField(
        verbose_name='about_me',
        max_length=512,
        blank=True
    )

    gender = models.CharField(
        verbose_name='gender',
        max_length=1,
        choices=GENDER_CHOISES,
        blank=True,
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()