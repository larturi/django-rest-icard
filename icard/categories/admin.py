from django.contrib import admin

from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )

    search_fields = ('title',)

admin.site.register(Category, CategoryAdmin)
