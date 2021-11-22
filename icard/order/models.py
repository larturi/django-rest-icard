from django.db import models
from django.db.models.base import Model

STATUS_ENUM = (
    ("PENDING", "pending"),
    ("DELIVERED", "delivered"),
)

class Order(models.Model):

    table = models.ForeignKey('table.Table', on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('product.product', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS_ENUM)
    created_at = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.table)