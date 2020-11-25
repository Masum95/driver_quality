from django.db.models import Q, QuerySet
from django.contrib.auth import get_user_model

from supply_order import models
from supply_order import enums

import datetime


class SupplyQuerySet(QuerySet):
    def get_order_between_dates(self, start_time, end_time):
        return self.filter(
            timestamp__range=[start_time, end_time]
        )

    def get_orders_aginst_supply_id(self, supply_id):
        return self.filter(
            supply_id=supply_id
        )

    def get_last_n_records(self, n):
        return self.order_by('-timestamp')[:int(n)]

    def get_completed(self):
        return self.filter(
            status=enums.StatusChoices.COMPLETED
        )


