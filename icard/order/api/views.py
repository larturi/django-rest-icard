from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.api.serializers import OrderSerializer

class OrderApiViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filterset_fields = ['category', 'active']