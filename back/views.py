from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth  import authenticate,login,logout
from back.forms.menu import MenuForm,SubMenuFormSet
from back.forms.newArticle import ArticleForm
from back.forms.newgallery import GalleryForm,GalleryImageFormset
from back.models import Image,Gallery
from django.db.models import Prefetch
from collections import defaultdict
# Create your views here.


def sayBye(request):
    return JsonResponse({
    "message": "Hello from backend",
    "status": "success"
})


def showTimeLine(request):
   
    galleries = Gallery.objects.prefetch_related(
        Prefetch('image_set', queryset=Image.objects.all())
    ).order_by('-creation_date')
    
    return render(request, 'back/timeline.html',{'galleries':galleries})


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
            for submenu in submenu_instances:
                submenu.menuRef = menu
                submenu.save()            

    return render(request, 'back/addmenu.html', {'form': menu_form, 'submenu_formset': submenu_formset})

def addGallery(request):
    # Initialize forms
    gallery_form = GalleryForm(request.POST or None)
    gallery_image_formset = GalleryImageFormset(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if gallery_form.is_valid() and gallery_image_formset.is_valid():
            # Save the gallery first
            gallery_instance = gallery_form.save()

            images_instances = gallery_image_formset.save(commit=False)
            if not images_instances:
                images_instances = [Image()]

            for idx, image in enumerate(images_instances):
                print("X")
                image_files = request.FILES.getlist(f'image_{idx+1}')  # 'image_{idx+1}' corresponds to input names
                for image_file in image_files:
                    # Create a new image object for each uploaded file
                    gallery_image = Image.objects.create(
                        image=image_file,
                        gallery=gallery_instance
                    )
                    gallery_image.save()  # Save the gallery image instance

            return redirect('gallery_list')  # Redirect after successful save

    else:
       
        gallery_form = GalleryForm()
        gallery_image_formset = GalleryImageFormset(queryset=Image.objects.none())

    return render(request, 'back/addgalary.html', {
        'gallery_form': gallery_form,
        'gallery_image_formset': gallery_image_formset
    })
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



  


