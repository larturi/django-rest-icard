from rest_framework.viewsets import ModelViewSet

from payment.models import Payment
from payment.api.serializers import PaymentSerializer

class PaymentApiView(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()