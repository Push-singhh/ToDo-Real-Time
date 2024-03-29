from django.db.models import F
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import Task
from category.models import Category


@receiver(post_save, sender=Task)
def increase_num_of_active_task_in_category(sender, instance, created, **kwargs):
    if created:
        Category.objects.filter(id=instance.category.id).update(num_of_active_task=F("num_of_active_task") + 1)


@receiver(post_delete, sender=Task)
def decrease_num_of_active_task_in_category(sender, instance, **kwargs):
    if instance.completed_at is None:
        Category.objects.filter(id=instance.category.id).update(num_of_active_task=F("num_of_active_task") - 1)
