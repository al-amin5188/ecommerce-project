from django.urls import path
from . import views

urlpatterns = [
    path('check-out/', views.check_out, name="check-out"),
    path('create-order', views.create_order, name='create-order'),
    path('add-order-items/<int:order_id>/', views.add_order_items, name='add-order-items'),
    path('my-orders/', views.user_orders , name='my-orders'),
    path('order-summary/<int:order_id>/', views.order_summary, name='order-summary'),
  
]
