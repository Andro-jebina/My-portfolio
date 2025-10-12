
from django.contrib import admin
from django.urls import path, include
from Jebina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('skill/', views.skill, name='skill'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),
    
]
