from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Product, Category, SubscriptionEmail, Slider
from django.core.paginator import Paginator
from review.models import Review
from user_profile.models import Profile
from django.db.models import Avg
from django.db.models import Q


# Home page views created here 
def home(request):
    featured_categories = Category.objects.filter(featured=True)
    featured_products = Product.objects.filter(featured=True)
    sliders = Slider.objects.filter(show=True)
    reviews = Review.objects.all()

    context = {
        'featured_categories':featured_categories,
        'featured_products':featured_products,
        'sliders':sliders,
        'reviews':reviews,
    }
    return render(request,'home/home.html' , context)


# Subscribe Email 
def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')

        if SubscriptionEmail.objects.filter(email=email).exists():
            messages.error(request, "You have already subscribed!")

        else:
            SubscriptionEmail.objects.create(email=email)
            messages.success(request, "Subscribed successfully!")
        
        return redirect('home')  
        
    return render(request, 'home/home.html')


#Shop Page Views Here
def shop_page(request):
    query = request.GET.get('q')
    products = Product.objects.all()
    categories = Category.objects.all()

    # Filtering by search query
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    # Sort by
    sort_option = request.GET.get('sort','')

    if sort_option == 'order':
        products = product.order_by('-id')
    elif sort_option == 'new':
        products = product.order_by('-created_date')
    elif sort_option == 'price':
        products = product.order_by('-price')
    

    # Paginator
    paginator = Paginator(products, 12)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Context
    context = {
        'products': page_obj, 
        'categories': categories,
        'query': query,
        'page_obj': page_obj,  
        'sort_option':sort_option,   
    }
    return render (request, 'shop/shop_page.html', context)


# Categories views
def categories_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    
    context = {
        'category': category,
        'products': products,
    }

    if not products:
        return redirect('no_result')
    
    return render(request, 'shop/categories.html', context)


# No Resul Views
def no_result(request):
    return render(request,'base/empty.html')


# Product Page Views 
def product_page(request,slug):
    product = get_object_or_404(Product, slug=slug) 
    category= product.category
    reviews = product.reviews.all() 
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    related_products = Product.objects.filter(category=category)

     

    context ={
        'product':product,
        'reviews':reviews,
        'ratings':average_rating,
        'related_products':related_products,
    }

    return render(request, 'shop/product_page.html', context)

