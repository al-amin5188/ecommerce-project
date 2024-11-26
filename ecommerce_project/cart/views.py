from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, WishList
from shop.models import Product

from decimal import Decimal


# Add To Cart 
@login_required(login_url='/user/login/')
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Check if product already exists in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request,'Product Added to Cart Successfully')
    return redirect('cart_page')


# Remove item from cart
@login_required(login_url='/user/login/')
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)

    cart_item.delete()

    messages.error(request,'Product Delete from Cart Successfully')
    return redirect('cart_page')


# Clear all Item 
@login_required(login_url='/user/login/')
def clear_cart(request):
    cart = get_object_or_404(Cart, user=request.user)

    # Clear all items from the cart
    CartItem.objects.filter(cart=cart).delete()

    messages.error(request,'All Product are Successfully Deleted')
    return redirect ('cart_page')


# Cart Page views here.
@login_required(login_url='/user/login/')
def cart_page(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    total_price = sum(item.total_price() for item in cart.items.all())
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping = subtotal * Decimal('0.1') 
    descount = subtotal * Decimal ('0.05')
    total_with_shipping = subtotal + shipping - descount

    context ={
        'cart':cart,
        'total_price':total_price,
        'subtotal': subtotal,
        'descount': descount,
        'shipping': shipping,
        'total': total_with_shipping,
    }

    return render (request,'cart/cart_page.html' , context)


# Update Cart
@login_required(login_url='/user/login/')
def update_quantity(request, product_id, quantity):
    quantity = int(quantity) 
    product = get_object_or_404(Product, id=product_id)
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    cart_item.quantity += quantity
    
    if cart_item.quantity <= 0:
        cart_item.delete()
        messages.error(request,'Product Delete to Cart Successfully')
    else:
        cart_item.save()
        
    
    return redirect('cart_page')


# Wish List views
@login_required
def wish_list(request):
    wishlist = get_object_or_404(WishList, user=request.user) 
    products = wishlist.products.all()

    context = {
        'wishlist': products,
    }

    return render(request, 'cart/wish_list.html', context)


#Add to WishList 
@login_required
def add_to_wishlist(request, slug):
    
    product = get_object_or_404(Product, slug=slug)
    wishlist, created = WishList.objects.get_or_create(user=request.user)
    wishlist.products.add(product)

    messages.success(request,'Add To Wish List !')
    return redirect('wish-list')


# Remove From WishList 
@login_required
def remove_from_wishlist(request, slug):
    product = get_object_or_404(Product, slug=slug)
    wishlist = WishList.objects.filter(user=request.user).first()
    if wishlist:
        wishlist.products.remove(product)

        messages.error(request,'Remove from wish list !')
    return redirect('wish-list')