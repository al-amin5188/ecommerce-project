from django.urls import path
from . import views

urlpatterns = [
    path('payment-menu/', views.payment_menu, name='payment-menu'),
    path('payment/form/<int:order_id>/', views.payment_form, name='payment_form'),
    path('payment/process/<int:payment_order_id>/', views.process_payment, name='process_payment'),
    path('payment/success/<int:payment_order_id>/', views.payment_success, name='payment_success'),
    path('payment/failure/<int:payment_order_id>/', views.payment_failure, name='payment_failure'),

    path('check_out/', views.check_out_page , name='check_out')
]
