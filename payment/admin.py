from django.contrib import admin
from .models import PaymentOrder

# Register your models here.


class PaymentOrderAdmin(admin.ModelAdmin):
    list_display=('order', 'total_price','payment_status','transaction_id','payment_method', 'created_at')

admin.site.register(PaymentOrder,PaymentOrderAdmin)