from django import forms 

from app3.models import Gallery, Studentsid,Negister

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)
    class Meta():
        model=Negister
        fields=('Email','Password')

class RegisterForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)
    class Meta():
        model=Negister
        fields='__all__'
        
class UpdateForm(forms.ModelForm):
    class Meta():
        model=Negister
        fields=('Name','Age','Place','Email')


class PasswordChangeForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=4)

class GalleryForm(forms.ModelForm):
    class Meta():
       model=Gallery
       fields='__all__'