from django import forms
from .models import Contact

class CreateContactForm(forms.Form):
    name = forms.CharField(label='Name')
    address = forms.CharField(widget=forms.Textarea, label='Address')
    profession = forms.CharField(label='Profession')
    tel_number = forms.CharField(label='Tel Number')
    email = forms.EmailField(label='Email')

class EditContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
