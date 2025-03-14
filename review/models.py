from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from user_profile.models import Profile


# Create your models here.

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1) 
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    picture= models.ImageField(upload_to='review/', blank=True, null=True)
   

    def __str__(self):
        return f"{self.user.username} - {self.rating}"

    class Meta:
        unique_together = ('product', 'user') 
