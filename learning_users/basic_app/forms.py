
from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
   

    # class Meta():
    #     model = UserProfileInfo
    #     exclude = ('user',)

    #kopinta

    class Meta():
       model = User
       fields = ('username','email','password')
    
# class UserProfileInfoForm(forms.ModelForm):
#      class Meta():
#          fields = ('portfolio_site', 'profile_pics')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')