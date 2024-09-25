from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    
    list_display = ( "name",
        "price",
        "description",
        "address",
    )
    list_filter = ("price", "address")
    search_fields = ("address",)