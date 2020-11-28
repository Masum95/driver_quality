from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.decorators import api_view

from supply_order import models, enums
from supply_order import serializers
from supply_order import pagination
from supply_order import parameters
from supply_order import utils
count_response = openapi.Response('response description', serializers.CountOrderSerializer)
get_list_response = openapi.Response('response description', serializers.SupplyOrderSerializer)


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
            queryset = queryset.get_orders_against_supply_id(supply_id=query_params.get('supply_id'))
        if 'how_many_last' in query_params:
            queryset = queryset.get_last_n_records(n=query_params.get('how_many_last'))
        return queryset

    @swagger_auto_schema(manual_parameters=[parameters.SUPPLY_ID_QUERY_PARAMETER,
                                            parameters.HOW_MANY_LAST_QUERY_PARAMETER],
                         responses={200: get_list_response})
    def get(self, request, *args, **kwargs):
        return super(SupplyOrderListCreateAPIView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SupplyOrderListCreateAPIView, self).post(request, *args, **kwargs)


@swagger_auto_schema(method='get', manual_parameters=[parameters.SUPPLY_ID_QUERY_PARAMETER,
                                                      parameters.HOW_MANY_LAST_QUERY_PARAMETER],
                     responses={200: count_response})
@api_view(['GET'])
def supply_order_count(request):
    """
        **returns completion rate for a particular user**
        Accepts two query params, supply_id : int
                                  how_many_last: int ( how many orders do you want to retrieve)
    """
    queryset = models.SupplyOrder.objects.all()
    query_params = request.GET
    how_many = str(100)

    if 'supply_id' in query_params:
        queryset = queryset.get_orders_against_supply_id(supply_id=query_params.get('supply_id'))

    if 'how_many_last' in query_params:
        how_many = query_params.get('how_many_last')

    queryset = queryset.get_last_n_records(n=how_many)

    # print(queryset)
    total, completed = 0, 0

    for row in list(queryset.values_list('status')):
        total += 1
        if row[0] == enums.StatusChoices.COMPLETED.value:
            completed += 1

    if total == 0:
        return JsonResponse({"error_message": "Sorry! Driver not found"}, safe=False, status=404)

    percent = completed / total
    print('completed: ', completed, 'total: ', total, 'percent: ', percent)
    if total < 100:
        percent = 0.85

    return JsonResponse({'percent': percent,
                         'message': utils.get_message(percent=percent)}, safe=False)
