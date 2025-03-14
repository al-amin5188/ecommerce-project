from django.contrib import admin
from . models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display=('product','user','rating','comment','created_at','picture')

admin.site.register(Review, ReviewAdmin)
