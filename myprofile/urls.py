
from django.contrib import admin
from django.urls import path, include
from Jebina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('certificate.html/', views.certificate, name='certificate'),
    path('project.html/', views.project, name='project'),
    path('contact.html/', views.contact, name='contact'),
    
]
