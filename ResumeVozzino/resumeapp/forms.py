from django.forms import ModelForm
from django import forms
from resumeapp.models import personaldetails
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class ResumeCreateForm(ModelForm):
    class Meta:
        model=personaldetails
        fields="__all__"
        widgets={


            "Email": forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Example: user@user.com'}),
            "Password": forms.PasswordInput(attrs={'class': 'form-control','placeholder' : 'Password'}),
            "Full_Name": forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Full Name '}),
            "Date_of_birth": forms.TextInput(attrs={'class': 'form-control','placeholder' : 'DD/MM/YYYY'}),
            "lastdegree": forms.TextInput(attrs={'class': 'form-control','placeholder' : 'your highest qualification'}),

        }



class ResumeEditForm(ModelForm):
    class Meta:
        model=personaldetails
        fields="__all__"
        widgets={


            "Email": forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Example: user@user.com'}),
            "Password": forms.PasswordInput(attrs={'class': 'form-control','placeholder' : 'Password'}),
            "Full_Name": forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Full Name '}),
            "Date_of_birth": forms.TextInput(attrs={'class': 'form-control','placeholder' : 'DD/MM/YYYY'}),
            "lastdegree": forms.TextInput(attrs={'class': 'form-control','placeholder' : 'your highest qualification'}),

        }


class Searchform(forms.Form):
    Full_Name=forms.CharField(max_length=120)

class Registrationform(UserCreationForm):
        class Meta:
            model = User
            fields = ["email", "username", "password1", "password2"]
            widgets = {

                "email": forms.TextInput(attrs={'class': 'form-control'}),
                "username": forms.TextInput(attrs={'class': 'form-control'}),
                "password1": forms.PasswordInput(attrs={'class': 'form-control'}),
                "password2": forms.PasswordInput(attrs={'class': 'form-control'}),


            }
