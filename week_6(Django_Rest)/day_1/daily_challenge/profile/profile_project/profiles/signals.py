from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=Profile)
def notify_new_profile(sender, instance, created, **kwargs):
    if created:
        print(f'New profile – Name: {instance.name}, Email: {instance.email}')


@receiver(pre_delete, sender=Profile)
def warn_before_deleting(sender, instance, **kwargs):
    if instance.is_active:
        print(f'Danger! You are deleting important info – Name: {instance.name}, Email: {instance.email}')