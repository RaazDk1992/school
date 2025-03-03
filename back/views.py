from django.shortcuts import render
from django.http import HttpResponse

from back.forms.menu import MenuForm

# Create your views here.

def sayBye(request):
    return HttpResponse('Bye')

def addMenu(request):
    menuForm = MenuForm()
    return render(request,'back/addmenu.html')
