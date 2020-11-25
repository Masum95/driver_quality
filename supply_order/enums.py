from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

#
# class Statushoices(TextChoices):
#     COMPLETED = 'COMPLETED', _('CANCELLED')
#     CANCELLED = 'CANCELLED', _('CANCELLED')


class StatusChoices(TextChoices):
    COMPLETED = 'COM', _('CANCELLED')
    CANCELLED = 'CAN', _('CANCELLED')

