from django.contrib import admin

from .models import Table

class TableAdmin(admin.ModelAdmin):
    list_display = (
        'number',
    )

admin.site.register(Table, TableAdmin)
