from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def products(request):
    product_items = [
        {'name': 'leptop', 'price': 2500},
        {'name': 'mouse', 'price': 80},
        {'name': 'keyboard', 'price': 200},
        {'name': 'monitor', 'price': 150},
        {'name': 'headphones', 'price': 100},
        {'name': 'phone', 'price': 1400},
    ]

    context = {
        "product_items": product_items,
    }

    return render(request, 'products.html', context)
