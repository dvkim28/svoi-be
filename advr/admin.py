from django.contrib import admin

from advr.models import Category


# Register your models here.


@admin.register(Category)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
