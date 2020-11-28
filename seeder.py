
from supply_order import enums
from supply_order.models import SupplyOrder

import datetime


def create_supply_order(timestamp, supply_id, order_id, status):
    SupplyOrder.objects.create(
        timestamp=timestamp,
        supply_id=supply_id,
        order_id=order_id,
        status=status
    )


comp_order_count = [85, 70, 50, 50, 50]
can_order_count = [25, 40, 50, 30, 0]
NUM_USERS = len(comp_order_count)  # 5

global_order_id = 1

base_date = '2008-05-01 12:01:00'
base_date = datetime.datetime.strptime(base_date, "%Y-%m-%d %H:%M:%S")

for i in range(NUM_USERS):
    supply_id = i + 1000
    day_cnt = 0
    for order in range(comp_order_count[i]):
        dt = base_date + datetime.timedelta(days=day_cnt)
        order_id = 'ord' + str(global_order_id)
        create_supply_order(dt, supply_id, order_id, enums.StatusChoices.COMPLETED)
        global_order_id += 1
        day_cnt += 1

    for order in range(can_order_count[i]):
        dt = base_date + datetime.timedelta(days=day_cnt)
        order_id = 'ord' + str(global_order_id)
        create_supply_order(dt, supply_id, order_id, enums.StatusChoices.CANCELLED)
        global_order_id += 1
        day_cnt += 1

