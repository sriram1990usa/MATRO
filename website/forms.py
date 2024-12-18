from django import forms
from website.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class contacts(forms.ModelForm):
    class Meta:
        model=contactus
        fields='__all__'
        
        
class searches(forms.ModelForm):
    class Meta:
        model=serch
        fields='__all__'
        
class searchsform(forms.ModelForm):
    class Meta:
        model=Searchs
        fields=('Pic1','Pic2','name','Maritial_status','Gender','age','religion','education','occupation','lastname','email','password','profileby','complexion','height','weight','approval','user',)     
        
        
class loginform(UserCreationForm):
    class Meta:
        model=User
        fields=('email','username','password1','password2',)

        
        
class storie(forms.ModelForm):
    class Meta:
        model=story
        fields='__all__'

'''
class sform(forms.ModelForm):
    class Meta:
        model=Shortlist
        fields='__all__
'''