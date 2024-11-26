from django.contrib import admin
from . models import Order, OrderItem, ShippingAddress

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_price','coupon_code' ,'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'coupon_code')

class OrderItemAdmin(admin.ModelAdmin):
    list_display=('order','product','quantity','unit_price','total_price')

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('order','name','phone_number', 'address', 'city', 'postal_code', 'country', )


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)