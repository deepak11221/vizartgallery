from django import forms
from .models import profile

class  profileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ('name','email','phone','address','city','state','pincode',)