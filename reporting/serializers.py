from rest_framework import serializers

from reporting.models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'description', 'created_time', 'amount']