from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'table',
        'product',
        'status',
        'created_at',
        'closed',
    )

    search_fields = ('product',)
    list_filter = ('table',)

admin.site.register(Order, OrderAdmin)
