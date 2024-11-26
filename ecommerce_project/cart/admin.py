from django.contrib import admin
from . models import Cart, CartItem, WishList
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display=('user','created_at')

class CartItemAdmin(admin.ModelAdmin):
    list_display=('cart','product','quantity')

class WishListAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_product_count', 'created_at')

    def get_product_count(self, obj):
        return obj.products.count()
    get_product_count.short_description = 'Number of Products'

admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(WishList, WishListAdmin)