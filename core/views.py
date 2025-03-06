from django.shortcuts import render
from items.models import Category,Item

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    category = Category.objects.all()
    return render(request, 'core/index.html',{
        'category': category,
        'items' : items,
    })

def contact(request):
    return render(request, 'core/contact.html')