from django.contrib import admin

from ordersapp.models import OrderItem, Order

admin.site.register(Order)
admin.site.register(OrderItem)