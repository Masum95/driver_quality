import json

# from coreapp.pagination import CustomPagination
from rest_framework import generics

from supply_order import models
from supply_order import serializers

class SupplyOrderListCreateAPIView(generics.ListCreateAPIView):

    """
        **List/Create Feedback**
    """
    serializer_class = serializers.SupplyOrderSerializer
    # pagination_class = pagination.CustomPagination
    queryset = models.SupplyOrder.objects.all()

    # todo: make search query_param to search_text
    # todo: add swagger doc
    def filter_queryset(self, queryset):
        query_params = self.request.query_params
        if 'search' in query_params:
            queryset = queryset.search(search_text=query_params.get('search'))
        if 'address' in query_params:
            queryset = queryset.address(address_uuid=query_params.get('address'))
        if 'country' in query_params:
            queryset = queryset.country(country=query_params.get('country'))
        if 'workplace' in query_params:
            queryset = queryset.workplace(workplace_uuid=query_params.get('workplace'))
        if 'department' in query_params or 'batch' in query_params:
            queryset = queryset.filter_by_batch_department(
                batch=query_params.get('batch'),
                department=query_params.get('department')
            )

        return queryset

    def get(self, request, *args, **kwargs):
        return super(SupplyOrderListCreateAPIView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(SupplyOrderListCreateAPIView, self).post(request, *args, **kwargs)