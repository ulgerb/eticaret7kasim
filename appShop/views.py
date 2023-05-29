from django.shortcuts import render

# Create your views here.


def shopPage(request):
   context = {}
   return render( request, "shop.html", context)

def detailPage(request):
   context = {}
   return render( request, "shop-single.html", context)