from django.shortcuts import render
from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    # Handle missing images
    for product in products:
        if not product.images:
            product.images = 'photos/default/default-image.png'  # Path to your default image

    context = {
        'products': products,
        'reviews': reviews,
    }
    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contact.html')