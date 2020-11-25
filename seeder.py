import os
import datetime
from django.utils import timezone

import django
# from datetime import datetime, time
from random import random
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "driver_quality.settings")

django.setup()

from supply_order.models import SupplyOrder
from random import randrange
from datetime import timedelta

def random_date():
    """
    This function will return a random datetime between two datetime
    objects.
    """
    end = timezone.now()
    start = end - datetime.timedelta(seconds=random.randint(0, 5 * 86400))
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)





def getRandomOrderStatus():
    k = random.randint(0, 1)  # decide on k once
    if k == 0:
        return "COMPLETED"
    return "CANCELLED"


def get_random_driver_id():
    k1 = random.randint(1000, 1003)  # decide on k once
    return k1

def populate_supply_order():

    for i in range(50):
        SupplyOrder.objects.create(
            timestamp=random_date(),
            supply_id=get_random_driver_id(),
            order_id='order'+str(i),
            status=getRandomOrderStatus()
        )


if __name__ == "__main__":
    populate_supply_order()