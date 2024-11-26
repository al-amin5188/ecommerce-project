from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart, CartItem
from .models import Order, OrderItem, ShippingAddress
from shop.models import Product
from decimal import Decimal
from django.db import transaction


# Chack Out Views
@login_required
def check_out(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        messages.error(request, "Your cart is empty!")
        return redirect('cart_page')

    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping = subtotal * Decimal('0.1') 
    discount = subtotal * Decimal ('0.05')
    total_with_shipping = subtotal + shipping - discount
    total_quantity = sum(item.quantity for item in cart_items)

    context = {
        'cart_items':cart_items,
        'subtotal':subtotal,
        'shipping':shipping,
        'discount':discount,
        'total':total_with_shipping,
        'total_quantity':total_quantity,

    }

    return render(request, 'order/check_out.html', context)


# Order Create views
@login_required
def create_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        messages.error(request, "Your cart is empty!")
        return redirect('cart_page')

    if request.method == 'POST':
        address = request.POST.get('address')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country', 'Bangladesh')
        payment = request.POST.get('option')

        if not payment:
            messages.error(request, "Payment option is required!")
            return redirect('check-out')

        
        with transaction.atomic():
            order = Order.objects.create(
                user=request.user,
                total_price=0,
            )

            ShippingAddress.objects.create(
                order=order,
                address=address,
                name=name,
                phone_number=phone_number,
                city=city,
                postal_code=postal_code,
                country=country
            )

            messages.success(request, "Shipping address added successfully!")

    total_price = 0
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping = subtotal * Decimal('0.1') 
    descount = subtotal * Decimal ('0.05')
    total_price = subtotal + shipping - descount
            
    order.total_price = total_price
    order.save()

            
           

    messages.success(request, "Order created successfully!")
    return redirect('add-order-items', order_id=order.id)


# Add OrderItem    
@login_required
def add_order_items(request, order_id):
    
    order = Order.objects.get(id=order_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    
    
    for item in cart_items:
        unit_price= item.product.price
        quantity= item.quantity
        total_price= unit_price * quantity

        OrderItem.objects.create(
            order=order,  
            product=item.product.name,
            quantity=quantity,
            unit_price=unit_price,
            total_price= total_price,
        )
    

    cart_items.delete()
    
    messages.success(request, "Order Created successfully!")
    return redirect('my-orders')


# User Order views
@login_required
def user_orders(request):
    order= Order.objects.filter(user=request.user)
    
    context={
        'orders': order.order_by('-id'),
    }

    return render(request, 'order/user_orders.html' , context)


# Order Summary views
@login_required
def order_summary(request,order_id):
    order = Order.objects.get(id=order_id)
    order_item = OrderItem.objects.filter(order=order)
    shippingAddress= ShippingAddress.objects.get(id=order_id)


    subtotal = sum(item.unit_price * item.quantity for item in order_item)
    shipping = subtotal * Decimal('0.1') 
    descount = subtotal * Decimal ('0.05')
    total_price = subtotal + shipping - descount
    
    context={
        'order': order,
        'order_items':order_item,
        'shippingAddress':shippingAddress,
        'subtotal':subtotal,
        'shipping': shipping,
        'descount':descount,
        'total_price': total_price,

    }

    return render(request, 'order/order_summary.html', context)




