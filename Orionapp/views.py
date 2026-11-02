from django.shortcuts import render, redirect, get_object_or_404
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

def delete(request, id):
    mycontact = Contact.objects.get(id=id)
    mycontact.delete()
    return redirect('/show')

def edit(request, id):
    editappointment = get_object_or_404(Contact, id=id)

    if request.method == 'POST':
        editappointment.name = request.POST.get('name')
        editappointment.email = request.POST.get('email')
        editappointment.subject = request.POST.get('subject')
        editappointment.message = request.POST.get('message')

        editappointment.save()
        return redirect('/show')

    else:
        return render(request, 'edit.html', {'editappointment': editappointment})
