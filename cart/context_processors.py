
from django.conf import settings
from . models import Cart

def cart_total_quantity(request):
    if not request.user.is_authenticated:
        return {'cart_total_quantity': 0}

    total_quantity = 0

    cart = Cart.objects.filter(user=request.user).first()
    if cart:
        total_quantity = sum(item.quantity for item in cart.items.all())

    
    return {'cart_total_quantity': total_quantity}
