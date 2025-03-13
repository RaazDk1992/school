from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.contrib.auth  import authenticate,login,logout
from back.forms.menu import MenuForm,SubMenuFormSet
from back.forms.newArticle import ArticleForm
from back.forms.newNotice import NoticeForm
from back.forms.messages import MessageForm
from back.forms.Dyamic import DynamicForm
from back.forms.contentTypes import ContentTypeForm
from back.forms.newgallery import GalleryForm,GalleryImageFormset
from back.forms.newslider import SliderForm,SliderFormSet
from back.models import Image,Gallery, Dynamic
from django.db.models import Prefetch
from collections import defaultdict

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
            print("Received POST data and validated")
            menu = menu_form.save()
            submenu_instances = submenu_formset.save(commit=False)
            for submenu in submenu_instances:
                submenu.menuRef = menu
                submenu.save()
            return redirect("success_url")  
        else:
            
            print("Menu Form Errors:", menu_form.errors)
            print("Submenu Formset Errors:", submenu_formset.errors)


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

def createContent(request):
    if request.user.is_authenticated:

        if request.method =="POST":
            form = DynamicForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
            return null
        else :
            dyn = DynamicForm()
            return render(request,'back/dynamic.html',{'form':dyn})
    else:
        return redirect('login')
    
def addContentType(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            frm = ContentTypeForm(request.POST or None)
            if frm.is_valid():
                frm.save()
        else:
            form = ContentTypeForm()
            return render(request,'back/contentType.html',{'form':form})
    else:
        return redirect('login') 
        

    
def dynamicView(request):

    path = request.path.rstrip('/').split('/')[-1] 
    print(path)
    #return render(request,'back/login.html')

def addSlider(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            formset  = SliderFormSet(request.POST,request.FILES)
            if formset.is_valid():
                for form in formset:
                    print(form)
                    if form.cleaned_data:
                        form.save()
        else:
            blank_formset = SliderFormSet()
            return render(request,'back/addslider.html',{'formset':blank_formset})
    else:
        return redirect('login')
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
    
def addNotice(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = NoticeForm(request.POST,request.FILES)
            if form.is_valid():
                notice = form.save()
                
                return JsonResponse({"message":f"Notice {notice.noticeTitle} published!!"},status=200)
            else:
               
                return JsonResponse({"message": "Error", "errors": form.errors}, status=400)

        if request.method =="GET":
            noticeForm =  NoticeForm()
            return render(request,'back/addnotice.html',{'form':noticeForm})
    else:
        return render(request,"back/addarticle.html")
    

def addMessage(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = MessageForm(request.POST,request.FILES)
            if form.is_valid():
                messagef = form.save()
        else:
            form = MessageForm()
            return render(request,"back/addMessage.html", {"form":form})
    else:
        return redirect('login')



def createUser(request):
    return render(request,"back/register.html")



  


