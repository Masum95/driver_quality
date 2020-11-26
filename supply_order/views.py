from django.http import JsonResponse
from rest_framework import generics

from supply_order import models, enums
from supply_order import serializers
from supply_order import pagination


class SupplyOrderListCreateAPIView(generics.ListCreateAPIView):

    """
        **List/Create SupplyOrder**
    """
    serializer_class = serializers.SupplyOrderSerializer
    pagination_class = pagination.CustomPagination
    queryset = models.SupplyOrder.objects.all()

    def filter_queryset(self, queryset):
        query_params = self.request.query_params
        if 'supply_id' in query_params:
            queryset = queryset.get_orders_aginst_supply_id(supply_id=query_params.get('supply_id'))
        if 'how_many_last' in query_params:
            queryset = queryset.get_last_n_records(n=query_params.get('how_many_last'))
        return queryset

    def get(self, request, *args, **kwargs):
        return super(SupplyOrderListCreateAPIView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SupplyOrderListCreateAPIView, self).post(request, *args, **kwargs)

def get_message(percent):
    if 0 <= percent <= 0.5:
        return """Your completion rate is very low.You will get suspended if you do
        not increase your completion rate."""

    if 0.51 <= percent <= 0.70:
        return """Your completion rate is low. You will get less requests if you do
                not increase your completion rate."""

    if 0.71 <= percent <= 1.0:
        return """Please complete more to get more
                requests."""


def supply_order_count(request):
    queryset = models.SupplyOrder.objects.all()
    query_params = request.GET

    if 'supply_id' in query_params:
        queryset = queryset.get_orders_aginst_supply_id(supply_id=query_params.get('supply_id'))

    if 'how_many_last' in query_params:
        queryset = queryset.get_last_n_records(n=query_params.get('how_many_last'))

    queryset_status = queryset.values('status')
    print(queryset.count())
    total = queryset.count()
    percent = 0
    if total == 0:
        return JsonResponse({"error_message": "Sorry! Driver not found"}, safe=False, status=404)
    elif total < 100:
        percent = 0.85
    else:
        completed = 0
        for row in list(queryset_status):
            if row['status'] == enums.StatusChoices.COMPLETED.name:
                completed += 1
        percent = completed/total

    return JsonResponse({'percent': percent,
                         'message': get_message(percent=percent)}, safe=False)  # or JsonResponse({'data': data})