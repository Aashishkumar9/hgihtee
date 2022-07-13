from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES=(
    ('lookbook','lookbook'),
    ('slider','slider')
)

class Products(models.Model):
    title=models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    productdetail=models.TextField()
    size_and_fit = models.CharField(max_length=100)
    material_and_care = models.CharField(max_length=100)
    product_img=models.ImageField(upload_to='product_img',blank = True)
    product_img1=models.ImageField(upload_to='product_img',blank = True)
    product_img2=models.ImageField(upload_to='product_img',blank = True)
    product_img3=models.ImageField(upload_to='product_img',blank = True)
    product_img4=models.ImageField(upload_to='product_img',blank = True)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
    ('S','S'),
    ('M','M'),
    ('L','L'),
    ('XL','XL'),
)

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    sizeofproduct=models.CharField(choices=CATEGORY_CHOICES,default='S',max_length=5)




STATE_CHOICE=(
    ('India','India'),
)

class Customeraddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    number=models.IntegerField()
    # dob=models.DateField()
    address=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(choices=STATE_CHOICE,default='India',max_length=100)
    pin_code=models.IntegerField()

    def __str__(self):
        return str(self.id)

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('Delivered','Delivered'),
)


class Orderplace(models.Model):
    sizeofproduct = models.CharField(max_length=10)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Customeraddress=models.ForeignKey(Customeraddress,on_delete=models.CASCADE)
    Product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')

    def __str__(self):
        return str(self.id)