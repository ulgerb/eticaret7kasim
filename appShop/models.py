from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Color(models.Model):
   title = models.CharField(("Renk"), max_length=50)
   slug = models.SlugField(("slug"), blank=True)
   
   def __str__(self):
      return self.title
   
   def save(self,*args,**kwargs):
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)
      
      
class Brand(models.Model):
   title = models.CharField(("Marka"), max_length=50)
   slug = models.SlugField(("slug"), blank=True)

   def save(self, *args, **kwargs):
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)
   
   def __str__(self):
      return self.title

class Category(models.Model):
   title = models.CharField(("Kategori"), max_length=50)
   slug = models.SlugField(("slug"), blank=True)

   def save(self, *args, **kwargs):
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)
   
   def __str__(self):
      return self.title



class Product(models.Model):
   user = models.ForeignKey( User, verbose_name=("Satıcı"), on_delete=models.CASCADE)
   category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
   brand = models.ForeignKey(Brand, verbose_name=("Marka"), on_delete=models.CASCADE)
   colors = models.ManyToManyField(Color, verbose_name=("Renkler"))
   title = models.CharField(("Ürün Başlık"), max_length=50)
   text = models.TextField(("Açıklama"), blank=True)
   price = models.FloatField(("Fiyat"))
   rating_total = models.FloatField(("Puanlama"), default=0)
   slug = models.SlugField(("slug"), blank=True)
   
   def save(self, *args, **kwargs):
      if Product.objects.all().exists():
         idp = Product.objects.last().id
      else:
         idp = 0
      if not self.slug:
         self.slug = slugify(self.title) + str(idp + 1)
      
      if not self.text:
         self.text = self.title
      super().save(*args, **kwargs)
   
   def __str__(self):
      return self.title

# class ProductDetail(models.Model):
#    product = 
#    color = 
#    stok = 
#    price = 
   
   

  
class Comment(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   product = models.ForeignKey(Product, verbose_name=("Ürün"), on_delete=models.CASCADE)
   title = models.CharField(("Yorum Başlık"), max_length=50,default="")
   text = models.TextField(("Yorum"), default="")
   rating = models.IntegerField(("Puan"), default=5)
   date_now = models.DateTimeField(("Tarih - Saat"), auto_now_add=True)
   
   def __str__(self):
      return self.title
   
   

