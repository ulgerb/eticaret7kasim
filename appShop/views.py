from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum


def shopPage(request):
   products = Product.objects.all()
   context = {
       "products": products,
   }
   return render( request, "shop.html", context)

def detailPage(request,slug, color):
   product = ProductDetail.objects.filter(product__slug=slug, color__slug=color)
   if product.exists():
      try:
         product = product.get()
      except:
         return redirect('/')
   listimage = len(ProductImage.objects.filter(product__slug=slug, color__slug=color))
   listimage =list(range(0,listimage,3))
   comments = Comment.objects.filter(product=product.product)
   

   if request.method =="POST":
      if request.user.is_authenticated:
         submit = request.POST.get("submit")

         if submit == "commentForm":
            rating = request.POST.get("rating")
            text = request.POST.get("text")

            comment = Comment(text = text, user=request.user, product=product.product)
            if rating is not None:
               comment.rating = rating
            comment.save()
            average_rating = comments.aggregate(Avg('rating'))['rating__avg']
            product.product.rating_total = round(average_rating, 1)      
            product.product.save()
         elif submit == "buyForm":
            piece = int(request.POST.get("piece"))
            shop = Shop.objects.filter(user=request.user, product=product)
            
            if not shop.exists():
               if 1<= piece <= product.stok:
                  shop = Shop(piece = piece, user=request.user, product=product)
                  shop.save()
               else:
                  messages.warning(request, 'Max ürün sayısını aştınız. alabileceğiniz mitar: '+ str(product.stok))
            else:
               if (shop.first().piece + piece) <= product.stok and 1 <= piece:
                  shop = shop.first()
                  shop.piece += piece 
                  shop.save()
               else:
                  messages.warning(request, 'Max ürün sayısını aştınız. ekleyebileceğiniz mitar: '+ str(product.stok - shop.first().piece ))
            
            
         return redirect('/detail/'+ product.product.slug +'/'+ color)
      
   context = {
      "product":product,
      "listimage": listimage,
      "comments": comments,
   }
   return render( request, "shop-single.html", context)


def shopBasketPage(request):
   shoping = Shop.objects.filter(user=request.user)
   total_price = 0
   for i in shoping:
      total_price += i.price
      
   if request.method == "POST":
      for k,v in request.POST.items():
         if k != "csrfmiddlewaretoken":
            shopid = k[5:]
            shopbasket = Shop.objects.get(id=shopid)
            if (int(v)) <= shopbasket.product.stok and 1 <= int(v):
               shopbasket.piece = v
               shopbasket.save()
            else:
               messages.warning(request, shopbasket.product.product.title+' Max ürün sayısını aştınız. ekleyebileceğiniz mitar: '+ str(shopbasket.product.stok - shopbasket.piece ))
      return redirect("shopBasketPage")
   
   context = {
       "shoping": shoping,
       "total_price": total_price,
   }
   return render(request, 'shop-basket.html', context)


def shopBasketDelete(request, id):
   shopbasket = Shop.objects.filter(id=id)
   if shopbasket.exists():
      shopbasket.first().delete()
   return redirect("shopBasketPage")

@login_required(login_url="/login")
def productAddPage(request):
   categorys = Category.objects.all()
   brands = Brand.objects.all()
   colors = Color.objects.all()
   colorsL = {}
   # select form
   for i,e in enumerate(colors):
      colorsL.update({i:  [e.title]})
   
   form = []
   color_list = []
   stok_list = []
   price_list = []
   image_list = []
   if request.method == "POST":
      submit = request.POST.get("submit")
      print(request.FILES)
      if submit == "productAddForm":
         for k,v in request.POST.items():
            if k != "csrfmiddlewaretoken" and k != "submit":
               color_list.append(v) if "color" in k else None
               stok_list.append(v) if "stok" in k else None
               price_list.append(v) if "price" in k else None
         imgfiles = list(request.FILES)
         say = 1
         print(imgfiles[-1][imgfiles[-1][8]:imgfiles[-1].find("_")])
         for k, v in request.FILES.items():
            imgs = []
            if "image"+str(say) in k:
               
               image_list.append()
            say+=1
               
         print(color_list, stok_list,price_list)
   context = {
       "categorys": categorys,
       "brands": brands,
       "colors": colors,
       "colorsL": colorsL,
   }
   return render(request, 'product-add.html', context)