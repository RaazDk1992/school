from django.shortcuts import render
from django.http import HttpResponse

from back.forms.menu import MenuForm
from back.forms.contenttype import ContentTypeForm

# Create your views here.

def sayBye(request):
    return HttpResponse('Bye')

def addMenu(request):
    menuForm = MenuForm()
    return render(request,'back/contenttype.html',{'form':menuForm})
def addContentType(request):
    contentTForm = ContentTypeForm()
    return render(request,'back/contenttype.html',{'form':contentTForm})


