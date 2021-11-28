from django.db import models

PAYMENT_TYPE_ENUM = (
    ('CARD', 'card'),
    ('CASH', 'cash'),
)

PAYMENT_STATUS_ENUM = (
    ('PENDING', 'pending'),
    ('PAID', 'paid'),
)

class Payment(models.Model):

    table = models.ForeignKey('table.table', on_delete=models.SET_NULL, null=True)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_TYPE_ENUM)
    status_payment = models.CharField(max_length=50, choices=PAYMENT_STATUS_ENUM)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str_(self):
        return self.table.name