from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_empty(request):
    return render(request, "empty.html")

def show_watchlist(request): # show watchlist in HTML
    context = {
        'name': 'Jonathan Adriel',
        'student_id': '2106750692',
        'watchlists': MyWatchList.objects.all()
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request): # show watchlist in XML
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")