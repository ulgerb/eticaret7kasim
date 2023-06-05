from django.contrib import admin
from .models import *

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
   list_display = ( 'title','id', 'user', 'product','rating')
   search_fields = ('title','user','product')
  
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ( 'title','id', 'user', 'category', 'brand','rating_total')
   search_fields = ('title','user','category','brand')
  
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
   list_display = ('product' , 'id','color') 
   search_fields = ('color',)
   
@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
   list_display = ('product', 'id', 'color', 'price')
   search_fields = ('color',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('title' , 'id',) 
   search_fields = ('title',)
  
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
   list_display = ('title' , 'id',) 
   search_fields = ('title',)
  
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
   list_display = ('title' , 'id',) 
   search_fields = ('title',)
  
  
