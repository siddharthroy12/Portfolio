from django.shortcuts import render
from .models import Project

def projects_view(request):
    context = {
        'projects': Project.objects.all(),
        'page': 'projects'
    }

    return render(request, 'projects/projects.html', context)