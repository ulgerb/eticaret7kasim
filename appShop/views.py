from django.shortcuts import render, get_object_or_404
from .models import *


def shopPage(request):
   products = Product.objects.all()
   context = {
       "products": products,
   }
   return render( request, "shop.html", context)

def detailPage(request,slug, color):
   product = ProductDetail.objects.filter(product__slug=slug, color__slug=color)
   listimage = len(ProductImage.objects.filter(product__slug=slug, color__slug=color))
   listimage =list(range(0,listimage,3))
   print(listimage)
   
   if product.exists():
      try:
         product = product.get()
      except:
         "hata"
   print(product)
   context = {
      "product":product,
      "listimage": listimage,
   }
   return render( request, "shop-single.html", context)