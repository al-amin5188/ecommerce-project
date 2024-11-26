from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<slug:slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('cart_page/',views.cart_page, name='cart_page'),
    path('update_quantity/<int:product_id>/<quantity>/', views.update_quantity, name='update_quantity'),


    #wish list
    path('wish-list/', views.wish_list, name='wish-list'),
    path('add-to-wishlist/<slug:slug>/',views.add_to_wishlist, name='add-to-wishlist'),
    path('remove-from-wishlist/<slug:slug>/', views.remove_from_wishlist , name='remove-from-wishlist')
]
