from django.contrib import admin
from .models import Products_Table, Cart_Table, Order_Table

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','details','brand','category','is_active','rating','image']

admin.site.register(Products_Table, ProductAdmin)
admin.site.register(Cart_Table)
admin.site.register(Order_Table)