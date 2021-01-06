from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'style': 'resize:none;', 'placeholder': 'Message', 'class': 'form-control'}))