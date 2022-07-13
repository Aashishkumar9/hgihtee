from locale import currency
from tkinter.messagebox import NO
from unicodedata import category
from django.shortcuts import render
from django.contrib.auth.views import PasswordChangeView,LoginView,LogoutView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView
from django.contrib import auth, messages
# from numpy import product
from .models import Products,Carts,Customeraddress,Orderplace
from django.http import HttpResponseRedirect, JsonResponse, request
from .forms import userresi,profilecustmerform,cartform
from django.views.generic.base import TemplateView,View
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.db.models import Q
import razorpay
from HGIH.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY


def home(request):
    slider = Products.objects.filter(category = 'slider')
    return render(request,'core/home.html',{'slider':slider})

def about(request):
    return render(request,'core/abouts_us.html')
    
def lookbook(request):
    data = Products.objects.all()
    return render(request,'core/lookbook.html',{'data':data})

def product_detail(request,pk):
    dt=Products.objects.get(pk=pk)
    # forms = sizeform
    return render(request, 'core/productdetails.html',{'product':dt})

def termsandcondition(request):
    return render(request,'core/termsandcondition.html')


class login(LoginView):
    template_name='core/login.html'
    success_url='/'

def add_to_cart(request):
    if request.user.is_authenticated:
        users=request.user
        product_i=request.GET.get('product_id')
        product=Products.objects.get(id=product_i)
        Carts(user=users,product=product).save()
        return redirect('/cart')
    return redirect('/accounts/login')
    

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


# def add_to_cart(request):
#     if request.user.is_authenticated:
#         users=request.user
#         product_i=request.GET.get('product_id')
#         product=Products.objects.get(id=product_i)
#         Cart(user=users,product=product).save()
#         return redirect('/cart')
#     return redirect('/accounts/login')

# def card(request):
#     forms = sizeform
#     return render(request,'core/card.html',{'forms':forms})


class customerregistration(View):
    def get(self,request):
        form=userresi()
        return render(request, 'core/registration.html',{'form':form})
    def post(self,request):
        form=userresi(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated.')
            return render(request, 'core/registration.html',{'form':form})
        return render(request, 'core/registration.html',{'form':form})
        
def custmeraddressview(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=profilecustmerform(request.POST)
            if fm.is_valid():
                usr=request.user
                fn=fm.cleaned_data['first_name']
                ln=fm.cleaned_data['last_name']
                em=fm.cleaned_data['email']
                number=fm.cleaned_data['number']
                # dob=fm.cleaned_data['dob']
                address=fm.cleaned_data['address']
                city=fm.cleaned_data['city']
                state=fm.cleaned_data['state']
                pin_code=fm.cleaned_data['pin_code']
                reg=Customeraddress(user=usr,first_name=fn,last_name=ln,email=em,number=number,address=address,city=city,state=state,pin_code=pin_code)
                reg.save()
                return HttpResponseRedirect('/checkout/')

        else:
            fm=profilecustmerform
        return render(request,'core/profile.html',{'form':fm,'active':'btn-primary'})
    return redirect('/accounts/login')
  

def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Carts.objects.filter(user=user)
        forms = cartform
        amount=0.0
        shopping_amount=100.0
        total_amount=0.0
        cart_product=[p for p in Carts.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.selling_price)
                amount +=tempamount
                total_amount=amount+shopping_amount
            return render(request, 'core/card.html',{'cart':cart,'total_amount':total_amount,'amount':amount,'shopping_amount':shopping_amount,'forms':forms})
        return render(request,'core/emptycart.html')
    return redirect('/accounts/login')

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Carts.objects.get(Q(product=prod_id) & Q(user=request.user))
        print(c,'-----------')
        # breakpoint()
        c.quantity+=1
        c.save()
        amount=0.0
        totalamount=0.0
        shopping_amount=100.0
        cart_product=[p for p in Carts.objects.all() if p.user==request.user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.selling_price)
                amount +=tempamount
                totalamount=amount+shopping_amount

                data = {
                    'quantity':c.quantity,
                    'amount':amount,
                    'totalamount':totalamount

                }
                return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Carts.objects.get(Q(product=prod_id) & Q(user=request.user))
        print(c,'-----------')
        # breakpoint()
        c.quantity-=1
        c.save()
        amount=0.0
        totalamount=0.0
        shopping_amount=100.0
        cart_product=[p for p in Carts.objects.all() if p.user==request.user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.selling_price)
                amount +=tempamount
                totalamount=amount+shopping_amount

                

                data = {
                    'quantity':c.quantity,
                    'amount':amount,
                    'totalamount':totalamount 

                }
                return JsonResponse(data)




def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Carts.objects.get(Q(product=prod_id) & Q(user=request.user))
        print(c,'-----------')
        # breakpoint()
        c.delete()
        amount=0.0
        totalamount=0.0
        shopping_amount=100.0
        cart_product=[p for p in Carts.objects.all() if p.user==request.user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity*p.product.selling_price)
                amount +=tempamount
                totalamount=amount+shopping_amount

  
                data = {
                    'amount':amount,
                    'totalamount':totalamount 

                }
                return JsonResponse(data)



# def checkout(request):
#     if request.user.is_authenticated:
#             user=request.user
#             address=Customeraddress.objects.filter(user=user)
#             # forms = Customeraddress()
#             cart=Carts.objects.filter(user=user)
#             amount=0.0
#             shipping_amount=100.0
#             total_amount=0.0
#             cart_product=[p for p in Carts.objects.all() if p.user==user]
#             if cart_product:
#                     for p in cart_product:
#                         tempamount=(p.quantity*p.product.selling_price)
#                         amount +=tempamount
#                     total_amount=amount+shipping_amount
#             return render(request, 'core/checkouts.html',{'cart':cart,'total_amount':total_amount,'address':address})
#     return redirect('/accounts/login')


def checkout(request):
    if request.user.is_authenticated:
            order_amount = 100
            order_currency = 'INR'
            payment_ordder = client.order.create(dict(amount = order_amount,currency=order_currency,payment_capture = 1))
            payment_order_id = payment_ordder['id']

            user=request.user
            address=Customeraddress.objects.filter(user=user)
            

            print(address,'address----------------------')
            cart=Carts.objects.filter(user=user)
            amount=0.0
            shipping_amount=100.0
            total_amount=0.0
            cart_product=[p for p in Carts.objects.all() if p.user==user]
            if cart_product:
                    for p in cart_product:
                        tempamount=(p.quantity*p.product.selling_price)
                        print(tempamount,'tempamount')
                        amount +=tempamount
                        print(amount,'amount')
                    total_amount=amount+shipping_amount

                    order_amount = total_amount*100
                    order_currency = 'INR'
                    payment_ordder = client.order.create(dict(amount = order_amount,currency=order_currency,payment_capture = 1))
                    payment_order_id = payment_ordder['id']

                    return render(request, 'core/checkouts.html',{'cart':cart,'add':address,'total_amount':total_amount,'amounts':amount,'amount':order_amount,'api_key':RAZORPAY_API_KEY,'order_id':payment_order_id})
    return redirect('/accounts/login')




client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
def payment(request):
    # if request.method == "POST":
            order_amount = 100
            order_currency = 'INR'
            payment_ordder = client.order.create(dict(amount = order_amount,currency=order_currency,payment_capture = 1))
            payment_order_id = payment_ordder['id']
            print(payment_order_id,'payment_order_id')
            return render(request,'core/pament.html',{'amount':1,'api_key':RAZORPAY_API_KEY,'order_id':payment_order_id})
    # return render(request,'core/pament.html',{'amount':1,'api_key':RAZORPAY_API_KEY,'order_id':payment_order_id})
import os
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# def payment(request):
#         amounts = 100 #100 here means 1 dollar,1 rupree if currency INR
#         client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
#         currency = 'INR'
#         # order_id
#         response = client.order.create({'amount':amounts,'currency':currency,'payment_capture':1})
#         print(response)
#         context = {'response':response}
#         return render(request,"core/pament.html",context)


@csrf_exempt
def payment_success(request):
    print('hello--------')
    # if request.user.is_authenticated:
    #     print('hello1--------')
    #     try:
    #         print('hello2--------')
    #         user=request.user
    #         custid=request.GET.get('custid')
    #         customer=Customeraddress.objects.get(id=custid)
    #         cart=Carts.objects.filter(user=user)
    #         print('---------------')
    #         for c in cart:
    #             print('-==================')
    #             print(Customeraddress,'Customeraddress')
    #             Orderplace(user=user,Customeraddress=customer,Product=c.product,quantity=c.quantity).save()
    #             c.delete()
    #         return redirect('orders')
    #     except:
    #         return HttpResponseRedirect('/checkout/')
    return redirect('/accounts/login')

    # if request.user.is_authenticated:
    #     try:
    #         user=request.user
    #         custid=request.GET.get('custid')
    #         customer=Customeraddress.objects.get(id=custid)
    #         cart=cart.objects.filter(user=user)
    #         for c in cart:
    #             Orderplace(user=user,customer=customer,Product=c.product,quantity=c.quantity).save()
    #             c.delete()
    #         return redirect('orders')
    #     except:
    #         return HttpResponseRedirect('/checkout/')
    # return redirect('/accounts/login')
    
def paymentdone(request):
    if request.user.is_authenticated:
        try:
            user=request.user
            custid=request.GET.get('custid')
            customer=Customeraddress.objects.get(id=custid)
            cart=Carts.objects.filter(user=user)
            for c in cart:
                print(Customeraddress,'Customeraddress')
                Orderplace(user=user,Customeraddress=customer,Product=c.product,quantity=c.quantity,sizeofproduct=c.sizeofproduct).save()
                c.delete()
            return redirect('orders')
        except:
            return HttpResponseRedirect('/checkout/')
    return redirect('/accounts/login')
  

def orders(request):
    if request.user.is_authenticated:
        dic=Orderplace.objects.filter(user=request.user)
        
        return render(request, 'core/orderdetail.html',{'op':dic})
    return redirect('/accounts/login')

    