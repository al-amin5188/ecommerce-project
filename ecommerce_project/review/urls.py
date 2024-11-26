from django.urls import path
from . import views

urlpatterns = [
    path('add-to-reviews/<slug:slug>/', views.add_to_reviews, name='add-to-reviews' ),

    path('product/<int:pk>/add_review/', views.add_review, name='add_review'),
    path('all_review/', views.review_list, name='review_list'),
]
