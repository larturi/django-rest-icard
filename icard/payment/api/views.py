from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from payment.models import Payment
from payment.api.serializers import PaymentSerializer

class PaymentApiView(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['table', 'status_payment', 'payment_type']
    ordering_fields = '__all__'