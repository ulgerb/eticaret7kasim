from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


def loginUser(request):
   context = {}
   
   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")

      user = authenticate(username=username, password=password)
      if user is not None:
         login(request, user)
      else:
         messages.warning(request, 'Kullanıcı adı veya şifre yanlış!')
         return redirect('loginUser')
      
      return redirect('indexPage')
      
   return render( request, "user/login.html", context)



def registerUser(request):
   context = {}
   
   if request.method == "POST":
      fname = request.POST.get("fname")
      email = request.POST.get("email")
      username = request.POST.get("username")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")

      if password1 == password2:
         if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
               user = User.objects.create_user(username=username, password=password1, first_name=fname, email=email)
               user.save()
               messages.success(request, 'Kaydınız başarıyla oluştu')
               return redirect('loginUser')
            else:
               messages.warning(request, 'Bu Email zaten kullanılıyor!')
               return redirect('registerUser')
         else:
            messages.warning(request, 'Bu username zaten başkası tarafından kullanılıyor!')
            return redirect('registerUser')
      else:
         messages.warning(request, 'Şifreler aynı değil!')
         return redirect('registerUser')
   return render( request, "user/register.html", context)


def logoutUser(request):
   logout(request)
   return redirect("indexPage")