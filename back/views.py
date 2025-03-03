from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sayBye(request):
    return HttpResponse('Bye')
