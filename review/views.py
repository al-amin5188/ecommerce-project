from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Review
from user_profile.models import Profile
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages


# Add Reviews
@login_required
def add_to_reviews(request, slug):
    product= get_object_or_404(Product, slug=slug)
    profile= get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if Review.objects.filter(product=product, user=request.user).exists():
            messages.error(request, "Alrady review exists !")
            return redirect('product-details', slug=slug)

        review = Review(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment,
            picture= profile.profile_picture
        )
        review.save()  
        messages.success(request, " Review Submited Successfully !")

    return redirect('product-details' ,slug=slug)  


@login_required
def add_review(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                return redirect('product_detail', pk=pk)

            except IntegrityError:
                messages.error(request, "Alrady done")
                return redirect(reverse('product_detail', kwargs={'pk': pk}))
    else:
        form = ReviewForm()
    return render(request, 'review/add_review.html', {'form': form, 'product': product})


def review_list(request):
    reviews = Review.objects.all()

    # গড় রেটিং হিসাব করা
    total_rating = sum(review.rating for review in reviews)
    avg_rating = total_rating / len(reviews) if reviews else 0

    sort_by = request.GET.get('sort', 'created_at')
    if sort_by == 'rating':
        reviews = reviews.order_by('-rating')
    else:
        reviews = reviews.order_by('-created_at')

    range_for_stars = range(5)
    return render(request, 'review/review_list.html', {
        'reviews': reviews,
        'avg_rating': round(avg_rating, 1),  # গড় রেটিং দশমিক পর্যন্ত
        'range_for_stars': range_for_stars,
    })

