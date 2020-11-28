
from rest_framework import serializers

from supply_order import models


class CountOrderSerializer(serializers.Serializer):
    percent = serializers.DecimalField(max_digits=3, decimal_places=2)
    message = serializers.CharField()


class SupplyOrderSerializer(serializers.ModelSerializer):
    """
    Serializer class for supply order.
    """

    class Meta:
        model = models.SupplyOrder
        # fields = '__all__'
        exclude = ['id']
