from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class StatusChoices(TextChoices):
    COMPLETED = 'COM', _('COMPLETED')
    CANCELLED = 'CAN', _('CANCELLED')

