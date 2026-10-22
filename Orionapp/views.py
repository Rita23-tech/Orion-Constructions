from django.shortcuts import render, redirect
from Orionapp.models import *
# Create your views here.

def home(request):
    if request.method == 'POST':
        mycontact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            message = request.POST['message'],
        )
        mycontact.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def show(request): #this helps the admin view everythong on contacts from the frontend
    all = Contact.objects.all()
    return render(request, 'show.html', {'all' : all})


