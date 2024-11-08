from django.db.models.signals import post_save
from django.dispatch import receiver
from riders.models import Rider
from .models import Lease

@receiver(post_save, sender=Rider)
def create_lease_for_new_rider(sender, instance, created, **kwargs):
    if created:
        Lease.objects.create(rider=instance)
