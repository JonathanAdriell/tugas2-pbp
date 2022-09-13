from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.

def show_catalog(request):
    context = {
        'name': 'Jonathan Adriel',
        'student_id': "2106750692",
        'catalog_list': CatalogItem.objects.all(),
    }
    return render(request, "katalog.html", context)