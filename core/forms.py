from cProfile import label
from pyexpat import model
from django import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django import forms
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm,PasswordResetForm,SetPasswordForm,password_validation
from django.contrib.auth.forms import AuthenticationForm,UsernameField,_
from razorpay import Card
from .models import Carts, Customeraddress


class login(AuthenticationForm):
      username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'usernamepass','class':'form-control'}))
      password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),
    )

class userresi(UserCreationForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model=User
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


# class sizeform(forms.ModelForm):
#     class Meta:
#         model = Card
#         fields=['sizeofproduct']
#         labels = {'sizeofproduct':''}

class profilecustmerform(forms.ModelForm):
    class Meta:
        model = Customeraddress
        fields=['first_name','last_name','email','number','address','city','state','pin_code']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'number':forms.NumberInput(attrs={'class':'form-control'}),
            # 'dob':forms.DateInput(attrs={'class':'DatePickerInput'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
           'state':forms.Select(attrs={'class':'form-label'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin_code':forms.NumberInput(attrs={'class':'form-control'}),
            }



class cartform(forms.ModelForm):
    class Meta:
        model = Carts
        fields = ['sizeofproduct']
        widgets={
            'sizeofproduct':forms.RadioSelect()

        }
        # choices=FAVORITE_COLORS_CHOICES,
        labels  = {
            'sizeofproduct':''
        }