from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('shop_page/',views.shop_page, name='shop_page'),
    path('categories/<slug:slug>/',views.categories_page, name='categories'),
    path('no_result/', views.no_result , name='no_result'),
    path("product-details/<slug:slug>/",views.product_page, name="product-details"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
