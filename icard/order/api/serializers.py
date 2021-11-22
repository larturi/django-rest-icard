from rest_framework.serializers import ModelSerializer

from order.models import Order
from product.api.serializers import ProductSerializer
from table.api.serializers import TableSerializer

class OrderSerializer(ModelSerializer):

    product_data = ProductSerializer(source='product', read_only=True)
    table_data = TableSerializer(source='table', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 
            'status', 
            'table', 
            'product', 
            'closed', 
            'created_at',
            'product_data',
            'table_data',
        ]