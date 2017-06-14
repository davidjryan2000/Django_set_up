from django.shortcuts import render
from .models import Contact


def say_hello(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts_list': contacts})


# Create your views here.
