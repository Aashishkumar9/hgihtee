from django.contrib import admin
from .models import Products,Carts,Customeraddress,Orderplace
# Register your models here.
@admin.register(Products)
class productadmin(admin.ModelAdmin):
    list_display  = ['id','title','brand','selling_price','discounted_price','productdetail','size_and_fit','material_and_care','product_img','product_img1','product_img2','product_img3','product_img4']

@admin.register(Carts)
class registercart(admin.ModelAdmin):
    list_display=['id','user','product','quantity','sizeofproduct']

@admin.register(Customeraddress)
class registercart(admin.ModelAdmin):
    list_display=['id','user','first_name','last_name','email','number','address','city','state','pin_code']

@admin.register(Orderplace)
class registerorderplace(admin.ModelAdmin):
    list_display=['id','user','Customeraddress','Product','quantity','order_date','status']
