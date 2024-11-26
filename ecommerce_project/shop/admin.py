from django.contrib import admin
from .models import Product, Category, Slider, Newsletter, SubscriptionEmail


# Admin Site views
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

class sliderAdmin(admin.ModelAdmin):
    list_display=('title', 'banner','show', 'created_date')    

class NewsletterAdmin(admin.ModelAdmin):
    list_display=('title','content','created_at')

class SubscriptionEmailAdmin(admin.ModelAdmin):
    list_display=('email','subscribed_at')

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Slider, sliderAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(SubscriptionEmail, SubscriptionEmailAdmin)


