from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from back.forms.menu import MenuForm
from back.forms.contenttype import ContentTypeForm

# Create your views here.


def sayBye(request):
    return JsonResponse({
    "message": "Hello from backend",
    "status": "success"
})


def login(request):
    return render(request,'back/login.html')

def createUser(request):
    return render(request,"back/register.html")

def addMenu(request):
    menuForm = MenuForm()
    return render(request,'back/contenttype.html',{'form':menuForm})
def addContentType(request):
    contentTForm = ContentTypeForm()
    return render(request,'back/contenttype.html',{'form':contentTForm})


