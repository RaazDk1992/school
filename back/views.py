from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth  import authenticate,login,logout
from back.forms.menu import MenuForm
from back.forms.newArticle import ArticleForm

# Create your views here.


def sayBye(request):
    return JsonResponse({
    "message": "Hello from backend",
    "status": "success"
})




def userLogin(request):
    if request.method == "POST":
        userName  = request.POST['username']
        password = request.POST['password']
        user =  authenticate(request,username=userName,password=password)
        if user is not None:
            login(request,user)
            return JsonResponse({"message":"Success"})
        else:
            return JsonResponse({"status":"failed","message":"Bad Credentials"})
    return render(request,'back/login.html')

def loadDashboard(request):
    if request.method =="GET":
        if request.user.is_authenticated:
            return render(request,"back/dashboard.html")
        else:
            return render(request,"back/login.html")
        

def addArticle(request):
    aticleForm =  ArticleForm()
    return render(request,'back/addarticle.html',{'form':aticleForm})

def createUser(request):
    return render(request,"back/register.html")



  


