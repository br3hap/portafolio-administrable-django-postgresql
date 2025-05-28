from django.shortcuts import render
from Base_App.models import *

# Create your views here.


def HomeView(request):
    person = Person.objects.all()
    projects = Project.objects.all()
    return render(request, 'home.html', {'person': person, 'projects': projects})


def FormTableView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = Form(name=name, email = email, subject = subject, message = message)

        data.save()
        person = Person.objects.all()
        projects = Project.objects.all()
        return render(request, 'home.html', {'person': person, 'projects': projects})