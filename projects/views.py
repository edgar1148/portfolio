from django.shortcuts import render, get_object_or_404

from .models import Projects

PROJECTS_PAGE = 6


def projects_view(request):
    projects = Projects.objects.order_by('-created_at')[:PROJECTS_PAGE]
    return render(request, 'index.html', {'projects': projects})

def about_view(request):
    return render(request, 'about.html')

def projects_detail_view(request, slug):
    projects = get_object_or_404(Projects, slug=slug)
    return render(request, 'projects_detail.html', {'projects': projects})

def сontacts_view(request):
    return render(request, 'contacts.html')