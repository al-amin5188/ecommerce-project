from django.db import models
from order.models import Order 

# Create your models here.

class PaymentOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        max_length=20,
        choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('FAILED', 'Failed')],
        default='PENDING'
    )
    transaction_id = models.CharField(max_length=100, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method= models.CharField(max_length=100)

    def __str__(self):
        return f"Payment Order {self.order.id} - {self.payment_status}"
