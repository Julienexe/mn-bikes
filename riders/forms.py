from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Lease, Rider, CustomUser


class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = '__all__'
        exclude= ('user',)
        
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = '__all__'

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

class LeaseForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = '__all__'
    
   