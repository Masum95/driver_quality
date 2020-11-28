from os import getenv

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from supply_order import enums
from supply_order.models import SupplyOrder
# from supply_order.tests import test_utils
# from supply_order.tests.populate_db import UserCreator, create_same_feedback
from supply_order import views

from datetime import datetime
from datetime import date, timedelta
import json


def create_supply_order(timestamp, supply_id, order_id, status):

    SupplyOrder.objects.create(
        timestamp= timestamp,
        supply_id= supply_id,
        order_id= order_id,
        status=status
    )


class SupplyOrderCountTestCase(APITestCase):
    """

    """

    def setUp(self):
        self.factory = APIRequestFactory()

        self.path = reverse('supply_order:supply_order_list_count')
        self.view = views.supply_order_count

    def test_get_supply_order_count(self):
        import datetime
        dt = datetime.datetime.strptime("2019-07-16 22:24:00", "%Y-%m-%d %H:%M:%S")

        comp_order_count = [85, 70, 50, 50, 50]
        can_order_count = [25, 40, 50, 30, 0]
        expected_percents = [0.75, 0.6, 0.5, 0.85, 0.85]
        NUM_USERS = len(comp_order_count) #5

        global_order_id = 1

        base_date = '2008-05-01 12:01:00'
        base_date = datetime.datetime.strptime(base_date, "%Y-%m-%d %H:%M:%S")

        for i in range( NUM_USERS):
            supply_id = i + 1000
            day_cnt = 0
            for order in range(comp_order_count[i]):
                dt = base_date + datetime.timedelta(days=day_cnt)
                order_id = 'ord' + str(global_order_id)
                create_supply_order(dt, supply_id, order_id, enums.StatusChoices.COMPLETED)
                global_order_id += 1
                day_cnt+=1

            for order in range(can_order_count[i]):
                dt = base_date + datetime.timedelta(days=day_cnt)
                order_id = 'ord' + str(global_order_id)
                create_supply_order(dt, supply_id, order_id, enums.StatusChoices.CANCELLED)
                global_order_id += 1
                day_cnt+=1

        for i in range(NUM_USERS):
            supply_id = i + 1000
            print(supply_id)
            query_params = 'supply_id=' + str(supply_id)
            request = self.factory.get(self.path + "?" + query_params)

            response = self.view(request)
            json_response = json.loads(response.content)
            print(response.content)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(float(json_response['percent']), expected_percents[i])
