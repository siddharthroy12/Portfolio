from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from portfolio import settings

def home(request):
    form = ContactForm()

    # If user submit contact form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # If form is valid send me email
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = f'{name} messaged you though your site.'
            form_subject = form.cleaned_data['subject']
            message = f'Subject: {form_subject}\n'
            message += f'Email: {email}\n'
            message += form.cleaned_data['message']
            send_mail(
                subject,
                message,
                form.cleaned_data['email'],
                [settings.EMAIL_AUTHOR],
                fail_silently=False,
            )
            form = ContactForm()
            messages.info(request, 'Message Sent Successfully')
    # Return clean form on GET request
    elif request.method == "GET":
        form = ContactForm()

    context = {
        "contact_form": form
    }

    return render(request, 'base/home.html', context)