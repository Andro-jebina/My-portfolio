from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def education(request):
    return render(request,'education.html')

def certificate(request):
    return render(request,'certificate.html')

def project(request):
    return render(request,'project.html')

def contact(request):
    return render(request,'contact.html')
