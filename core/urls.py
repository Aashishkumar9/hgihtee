"""HGIH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# from HGIH.core.views import lookbook
from core import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .forms import login

urlpatterns = [
    path('',views.home,name='home'),
    path('abouts/',views.about,name='about'),
    path('lookbook/',views.lookbook,name='lookbook'),
    path('product-detail/<int:pk>/', views.product_detail, name='product-detail'),
    path('accounts/login/',views.login.as_view(authentication_form=login), name='login'),
    path('accounts/logout/',views.logout, name='logout'),
    path('termsandcondition/',views.termsandcondition, name='termsandcondition'),
    path('registration/', views.customerregistration.as_view(), name='customerregistration'),
    # path('cart/', views.card, name='showcart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('profile/', views.custmeraddressview, name='profile'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='pament'),
    path('success/',views.payment_success,name="payment-success"),
    path('paymentdone/',views.paymentdone,name='paymentdone'),
    path('orders/',views.orders,name='orders'),






]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
