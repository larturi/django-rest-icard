from django.contrib import admin

from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'table',
        'total_payment',
        'payment_type',
        'status_payment',
        'created_at',
    )

    list_filter = ('table', 'status_payment', 'payment_type')

admin.site.register(Payment, PaymentAdmin)
