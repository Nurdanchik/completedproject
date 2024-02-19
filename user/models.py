from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def add_id_to_user(sender, instance, created, **kwargs):
    """
    Сигнал, вызываемый после сохранения объекта User.
    """
    if created:
        instance.id = instance.pk
        instance.save()
