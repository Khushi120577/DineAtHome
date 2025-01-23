from django.shortcuts import render
from adminapp.models import MenuCategory

def menu_view(request):
    categories = MenuCategory.objects.prefetch_related('menu_items').all()
    print(categories)  # Debugging: Check if categories are being fetched
    return render(request, 'menu.html', {'categories': categories})
