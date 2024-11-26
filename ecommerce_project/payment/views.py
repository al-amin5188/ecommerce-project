from django.shortcuts import render, redirect
from .models import PaymentOrder
from order.models import Order
import random
from django.contrib.auth.decorators import login_required


# Payment Page views


# Payment Page views here.
def check_out_page(request):
    return render(request,'payment/check_out.html')

@login_required
def payment_menu(request):
    orders = Order.objects.filter(user=request.user) 

    order_payment_status = []
    for order in orders:
        payment_order = PaymentOrder.objects.filter(order=order).order_by('-created_at').first()

        # PaymentOrder পাওয়া গেলে
        if payment_order:
            order_payment_status.append({
                'order': order,
                'payment_status': payment_order.payment_status,
                'amount': payment_order.total_price,  # PaymentOrder থেকে total_price ব্যবহার করুন
                'transaction_id': payment_order.transaction_id,
            })
        else:
            order_payment_status.append({
                'order': order,
                'payment_status': 'Not Found',
                'amount': 0,
                'transaction_id': None,
            })

    return render(request, 'payment/payment_menu.html', {'order_payment_status': order_payment_status})


def payment_form(request, order_id):
    order = Order.objects.get(id=order_id)
    payment_order = PaymentOrder.objects.create(order=order, total_price=order.total_price)
    return render(request, 'payment/payment_form.html', {'payment_order': payment_order})

# ফেক পেমেন্ট প্রক্রিয়া
def process_payment(request, payment_order_id):
    payment_order = PaymentOrder.objects.get(id=payment_order_id)
    
    # ফেক পেমেন্ট স্ট্যাটাস নির্ধারণ (Random success or failure)
    payment_status = random.choice(['PAID', 'FAILED'])
    payment_order.payment_status = payment_status
    payment_order.save()
    
    if payment_status == 'PAID':
        return redirect('payment_success', payment_order_id=payment_order.id)
    else:
        return redirect('payment_failure', payment_order_id=payment_order.id)

# পেমেন্ট সফল হলে কনফার্মেশন পেজ
def payment_success(request, payment_order_id):
    payment_order = PaymentOrder.objects.get(id=payment_order_id)
    return render(request, 'payment/payment_success.html', {'payment_order': payment_order})

# পেমেন্ট ব্যর্থ হলে কনফার্মেশন পেজ
def payment_failure(request, payment_order_id):
    payment_order = PaymentOrder.objects.get(id=payment_order_id)
    return render(request, 'payment/payment_failure.html', {'payment_order': payment_order})
