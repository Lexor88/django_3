from django.shortcuts import render
from .models import Product, Contact

def index(request):
    # Выборка последних пяти товаров
    latest_products = Product.objects.order_by('-created_at')[:5]

    # Вывод в консоль
    for product in latest_products:
        print(product.id, product.name, product.price)


    context = {
        'latest_products': latest_products,
    }
    return render(request, 'index.html', context)

def contact(request):
    contacts = Contact.objects.all()  # Получение всех контактов
    return render(request, 'contact.html', {'contacts': contacts})
