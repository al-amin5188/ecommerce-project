from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile_redirect/', views.profile_redirect, name='profile_redirect'),
    path('edite-profile/', views.edite_profile, name='edite-profile'),
    path('profile-view/', views.profile_view, name='profile-view'),
    path('profile-details/',views.profile_details, name='profile-details'),
    path('edite-profile-page/', views.edite_profile_page, name='edite-profile-page'),
    path('sitting/', views.sitting_page, name='sitting'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
