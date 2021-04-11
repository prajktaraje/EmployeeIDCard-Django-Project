from django import forms
from .models import Empid
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=Empid
        fields=['name','email','post','bloodgroup']

        widgets={
            'name':forms.TextInput( attrs={'class':'form-control','placeholder':"Enter your  Full Name",}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter your Email"}),
            'post':forms.TextInput( attrs={'class':'form-control','placeholder':"Enter your Post",}),
            'bloodgroup':forms.TextInput( attrs={'class':'form-control','placeholder':"Enter your Blood Group",}),
          
        }
