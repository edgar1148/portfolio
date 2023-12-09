from django.urls import path
from .views import projects_view, about_view, projects_detail_view, сontacts_view


app_name = 'projects'

urlpatterns = [
    path('', projects_view, name='projects'),
    path('about/', about_view, name='about'),
    path('projects/<slug:slug>/', projects_detail_view, name='projects-detail'),
    path('contacts/', сontacts_view, name='contacts'),
]