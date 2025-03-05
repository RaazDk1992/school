from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth  import authenticate,login,logout
from back.forms.menu import MenuForm,SubMenuFormSet
from back.forms.newArticle import ArticleForm

# Create your views here.


def sayBye(request):
    return JsonResponse({
    "message": "Hello from backend",
    "status": "success"
})


def showTimeLine(request):
    return render(request, 'back/timeline.html')


def userLogin(request):
    if request.method == "POST":
        userName  = request.POST['username']
        password = request.POST['password']
        user =  authenticate(request,username=userName,password=password)
        if user is not None:
            login(request,user)
            return JsonResponse({"message":"Success"},status=200)
        else:
            return JsonResponse({"status":"failed","message":"Bad Credentials"}, status=401)
    return render(request,'back/login.html')

def loadDashboard(request):
    if request.method =="GET":
        if request.user.is_authenticated:
            return render(request,"back/dashboard.html")
        else:
            return render(request,"back/login.html")
def addMenu(request):
    if not request.user.is_authenticated:
        return redirect('login')  

    menu_form = MenuForm(request.POST or None)
    submenu_formset = SubMenuFormSet(request.POST or None)

    if request.method == 'POST':
        if menu_form.is_valid() and submenu_formset.is_valid():
            menu = menu_form.save()
            submenu_instances = submenu_formset.save(commit=False) 
            print(submenu_instances)
            for submenu in submenu_instances:
                submenu.menuRef = menu
                submenu.save()  

            #submenu_formset.save_m2m()  # Ensure many-to-many fields are saved if any

            #return redirect('success_url')  # Redirect after saving

    return render(request, 'back/addmenu.html', {'form': menu_form, 'submenu_formset': submenu_formset})
def addArticle(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = ArticleForm(request.POST,request.FILES)
            if form.is_valid():
                article = form.save()
                
                return JsonResponse({"message":f"Article {article.title} published!!"},status=200)
            else:
               
                return JsonResponse({"message": "Error", "errors": form.errors}, status=400)

        if request.method =="GET":
            aticleForm =  ArticleForm()
            return render(request,'back/addarticle.html',{'form':aticleForm})
    else:
        return render(request,"back/addarticle.html")

def createUser(request):
    return render(request,"back/register.html")



  


