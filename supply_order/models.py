
# Create your models here.
import uuid


from django.db import models
from django.db.models import Model


from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils import timezone

from supply_order import enums, querysets
from supply_order.enums import *

# from .managers import *




class SupplyOrder(models.Model):
    puid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now=False)
    supply_id = models.BigIntegerField()
    order_id = models.CharField(max_length=128)
    status = models.CharField(
        max_length=4,
        choices=enums.StatusChoices.choices,
        blank=False
    )
    objects = querysets.SupplyQuerySet.as_manager()
    # def get_react_count(self):
    #     return self.reacts_set.count

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['timestamp']
        verbose_name = "SupplyOrder"
        verbose_name_plural = "SupplyOrders"
        indexes = [
            models.Index(fields=['timestamp']),
        ]

    def __str__(self):
        return "{driver}, {order_id}, {status}, {timestamp}".format(
            driver=self.supply_id,
            order_id=self.order_id,
            status=self.status,
            timestamp=self.timestamp
        )

    def get_absolute_url(self):
        return reverse("supply_order:supply_order_manipulate", kwargs={"uuid": self.uuid})
