from django.shortcuts import render

def home(response):
    return render(response, 'base/home.html')