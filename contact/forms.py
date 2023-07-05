from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name",required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'escribe tu nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget= forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'escribe tu email'}
    ), min_length=3 , max_length=100)
    content = forms.CharField(label="Content",required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':3, 'placeholder':'write please'}
    ),min_length=10, max_length=1000)