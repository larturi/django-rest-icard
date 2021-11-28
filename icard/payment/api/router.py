from rest_framework.routers import DefaultRouter

from payment.api.views import PaymentApiView

router_payments = DefaultRouter()

router_payments.register(
    prefix='payments',
    basename='payments',
    viewset=PaymentApiView
)