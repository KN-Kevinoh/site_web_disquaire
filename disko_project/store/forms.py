from django import forms
from django.forms.utils import ErrorList
from django.forms import ModelForm, TextInput, EmailInput
from .models import Contact


# here, we want display errors as paragraphs not as a list
class FormatErrorList(ErrorList):

    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self : return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<p class="error">%s</p>' % e for e in self])
    

# generate and validate forms

"""
class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
        )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
        )
"""
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email']
        widget = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'})
        }