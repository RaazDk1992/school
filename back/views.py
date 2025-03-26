from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.contrib.auth  import authenticate,login,logout
from back.forms.menu import MenuForm,SubMenuFormSet
from back.forms.newArticle import ArticleForm
from back.forms.newNotice import NoticeForm,NoticeImageForm,NoticeDocumentForm
from back.forms.editNotice import NoticeFormEdit,NoticeImageFormEdit,NoticeDocumentFormEdit
from back.forms.messages import MessageForm
from back.forms.Dyamic import DynamicForm
from back.forms.contentTypes import ContentTypeForm
from back.forms.newgallery import GalleryForm,GalleryImageFormset
from back.forms.editGallery import EditGalleryForm,EditGalleryImageFormset
from back.forms.Events import EventsForm
from back.forms.Testimonial import TestimonialForm
from back.forms.newslider import SliderForm,SliderFormSet
from back.models import Image,Gallery, Dynamic,Article,Notices,NoticeDocuments,NoticeImages,ContentType,Events
from django.db.models import Prefetch
from collections import defaultdict
import os
from django.forms import modelformset_factory

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
            article_list = Article.objects.all()
            notice_list = Notices.objects.all()
            gallery_list = Gallery.objects.all()

            ## get dynamically added elements
           
            dynamic_query_set = Dynamic.objects.all()
            contentTypes = ContentType.objects.prefetch_related(Prefetch('dynamic_set',queryset=dynamic_query_set)).all()
           
            context ={
                'article_list':article_list,
                'notice_list': notice_list,
                'gallery_list':gallery_list,
                'content_types':contentTypes
            }
            return render(request,"back/dashboard.html",context)
        else:
            return redirect('login')
        

def editDynamic(request, id):
   
   if request.user.is_authenticated:
       dynamicObject = get_object_or_404(Dynamic,id=id)

       if request.method =="POST":
            dynamicForm = DynamicForm(request.POST,request.FILES,instance=dynamicObject)
            if dynamicForm.is_valid():
                dynamicForm.save()
                return JsonResponse({'status':'Success','message':'Update successful!!'},status=200)
            else:
                return JsonResponse({'status':'fail','message':'Could not be updated','error':dynamicForm.errors},status=400)
       else:
           form  = DynamicForm(instance=dynamicObject)
           return render(request,"back/dynamic.html",{"form":form})
   else:
       return redirect('login')
       
def deleteDynamic(request,id):
    if request.user.is_authenticated:
        dynamicObject = get_object_or_404(Dynamic,id=id)
        
        if dynamicObject.owner != request.user:
            return JsonResponse({'status':'fail','message':'You are not authorized to delete this'},status=401)
        else:
            dynamicObject.delete()
            return JsonResponse({'status':'success', 'message':'Deletion Successful!!'},status=200)
    else:
        return redirect('login')

def deleteNotice(request,id):
    if request.user.is_authenticated:
        notice = get_object_or_404(Notices,id=id)

        if notice.owner != request.user:
            return JsonResponse({'status':'fail','message':'You are not authorized'},status=401)
        else:
            notice.delete()
            return JsonResponse({'status':'success','message':'Notice deleted'},status=200)

def deleteEvent(request,id):
    if request.user.is_authenticated:
        event = get_object_or_404(Events,id=id)
        if event.owner != request.user:
            return JsonResponse({'status':'fail','message':'You are not authorized to delete this'},status=200)
        else:
            event.delete()
            return JsonResponse({'status':'success','message':'Delete successfully!!'},status=200)

def deleteGallery(request,id):
    if request.user.is_authenticated:
        gallery = get_object_or_404(Gallery,id=id)
        if gallery.owner != request.user:
            return JsonResponse({'status':'fail','message':'You are not authorized to delete this'},status=401)
        else:
            gallery.delete()
            return JsonResponse({'status':'success','message':'Delete successfully!!'},status=200)
    
    
def editNotice(request, notice_id):
    if not request.user.is_authenticated:
        return redirect('login')

    # Fetch existing notice and related objects
    notice = get_object_or_404(Notices, id=notice_id)
    notice_documents = NoticeDocuments.objects.filter(notice=notice)
    notice_images = NoticeImages.objects.filter(notice=notice)

    # Determine the extra forms count
    extra_forms = 1 if not notice_documents.exists() and not notice_images.exists() else 0

    # Define formsets
    NoticeImageFormSet = modelformset_factory(NoticeImages, form=NoticeImageFormEdit, extra=extra_forms, can_delete=True)
    NoticeDocumentFormSet = modelformset_factory(NoticeDocuments, form=NoticeDocumentFormEdit, extra=extra_forms, can_delete=True)

    if request.method == "POST":
        form = NoticeFormEdit(request.POST, request.FILES, instance=notice)
        notice_document_formset = NoticeDocumentFormSet(request.POST, request.FILES, queryset=notice_documents, prefix="documents")
        notice_image_formset = NoticeImageFormSet(request.POST, request.FILES, queryset=notice_images, prefix="images")

        # Debugging: Check if formsets are receiving data
        print(f"POST Data: {request.POST}")  # Logs POST data
        print(f"Files: {request.FILES}")  # Logs uploaded files

        if form.is_valid() and notice_document_formset.is_valid() and notice_image_formset.is_valid():
            notice = form.save()  # Save the notice first

            # Assign notice to each document before saving
            for doc_form in notice_document_formset:
                if doc_form.instance.pk is None:  # Only for new instances
                    doc_form.instance.notice = notice
                    doc_form.instance.owner = request.user

            # Assign notice to each image before saving
            for img_form in notice_image_formset:
                if img_form.instance.pk is None:  # Only for new instances
                    img_form.instance.notice = notice
                    img_form.instance.owner=request.user

            notice_document_formset.save()
            notice_image_formset.save()

            return JsonResponse({'status': 'success', 'message': 'Notice updated successfully!'}, status=200)
        else:
            errors = []
            if form.errors:
                errors.extend([f"{field}: {error}" for field, error_list in form.errors.items() for error in error_list])
            if notice_document_formset.errors:
                for idx, form_errors in enumerate(notice_document_formset.errors):
                    errors.extend([f"Document {idx+1} - {field}: {error}" for field, error_list in form_errors.items() for error in error_list])
            if notice_image_formset.errors:
                for idx, form_errors in enumerate(notice_image_formset.errors):
                    errors.extend([f"Image {idx+1} - {field}: {error}" for field, error_list in form_errors.items() for error in error_list])

            return JsonResponse({'status': 'fail', 'message': 'Data could not be saved', 'errors': errors}, status=400)

    else:
        form = NoticeFormEdit(instance=notice)
        notice_document_formset = NoticeDocumentFormSet(queryset=notice_documents, prefix="documents")
        notice_image_formset = NoticeImageFormSet(queryset=notice_images, prefix="images")

    return render(request, 'back/editnotice.html', {
        'form': form,
        'notice_document_formset': notice_document_formset,
        'notice_image_formset': notice_image_formset,
    })
def edit_gallery(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id)
    images = Image.objects.filter(gallery=gallery)
    
    if request.method == "POST":
        gallery_form = EditGalleryForm(request.POST, instance=gallery)
        formset = EditGalleryImageFormset(request.POST, request.FILES, queryset=images)
        
        if gallery_form.is_valid() and formset.is_valid():
            gallery_form.save()
            for form in formset:
                if form.cleaned_data.get('DELETE'):
                    form.instance.delete()
                else:
                    image = form.save(commit=False)
                    image.gallery = gallery
                    image.save()
            return redirect('gallery_list')  # Redirect to gallery list or appropriate page
    else:
        gallery_form = EditGalleryForm(instance=gallery)
        formset = EditGalleryImageFormset(queryset=images)
    
        return render(request, "back/editgalary.html", {
            "gallery_form": gallery_form,
            "gallery_image_formset": formset,
        })


def addEvents(request):
    if not request.user.is_authenticated:
        return redirect('login') 

    if request.method == "POST":
       eventForm = EventsForm(request.POST)
       if eventForm.is_valid():
           obj = eventForm.save(commit=False)
           obj.owner = request.user
           obj.save()

    else:
        eventForm = EventsForm()
    return render(request, 'back/addevents.html', {'form': eventForm})

def addTestimonial(request):
    if request.user.is_authenticated:

        if request.method =="POST":
            testimonialForm = TestimonialForm(request.POST,request.FILES)
            if testimonialForm.is_valid():
                testimonialForm.save()
        else:
            form = TestimonialForm()
            return render(request,'back/addTestimonial.html',{'form':form})

    else:
        return redirect('login')

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
            return JsonResponse({'status':'success','message':'Menu item added successfully!!'},status=200)
        else:
            
            return JsonResponse({'status':'error','message':f'Could not create menu{menu_form.errors}'},status=400)


    return render(request, 'back/addmenu.html', {'form': menu_form, 'submenu_formset': submenu_formset})

def addGallery(request):
    # Initialize forms
    gallery_form = GalleryForm(request.POST or None)
    gallery_image_formset = GalleryImageFormset(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if gallery_form.is_valid() and gallery_image_formset.is_valid():
            # Save the gallery first
            gallery_instance = gallery_form.save(commit=False)
            gallery_instance.owner = request.user
            gallery_instance.save()

            images_instances = gallery_image_formset.save(commit=False)
            if not images_instances:
                images_instances = [Image()]

            for idx, image in enumerate(images_instances):
                image_files = request.FILES.getlist(f'image_{idx+1}')  
                for image_file in image_files:
                    # Create a new image object for each uploaded file
                    gallery_image = Image.objects.create(
                        image=image_file,
                        gallery=gallery_instance,
                        owner = request.user
                    )
                    gallery_image.save()  # Save the gallery image instance

            return JsonResponse({'status':'success','message':f'Gallery {gallery_instance.galleryName} created!!'}, status=200)
        else:
            return JsonResponse({'status':'fail','message':'Could not create gallery!!'}, status=400)

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
                instance = form.save(commit=False)
                instance.owner = request.user
                instance.save()
                return JsonResponse({'status':'success','message':'Item added'},status=200)
            else:
                return JsonResponse({'status':'fail','message':f'Could not be created{form.errors}'},status=400)
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
                instance = frm.save(commit=False)
                instance.owner = request.user
                instance.save()
                return JsonResponse({'status':'success','message':'contentType added!!'},status=200)
            else:
                return JsonResponse({'status':'failed','message':'failed to add contentType','error':frm.errors})
        else:
            form = ContentTypeForm()
            return render(request,'back/contentType.html',{'form':form})
    else:
        return redirect('login') 
        

    


def addSlider(request):
    if not request.user.is_authenticated:
        return redirect('login') 

    if request.method == "POST":
        formset = SliderFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    form.save()
            return JsonResponse({"message": "Sliders added successfully!"}, status=200)

        else:
            errors = {f"form_{i}": form.errors.as_json() for i, form in enumerate(formset) if form.errors}
            return JsonResponse({"error": "Validation failed", "errors": errors}, status=400)

    # Return formset for initial rendering
    blank_formset = SliderFormSet()
    return render(request, 'back/addslider.html', {'formset': blank_formset})

# Method to  add new article, if user is authenticated, check if form is valid, otherwise goto authentication
def addArticle(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = ArticleForm(request.POST,request.FILES)
            if form.is_valid():
                article = form.save(commit=False)
                article.owner = request.user
                article.save()
                
                return JsonResponse({"message":f"Article {article.title} published!!"},status=200)
            else:
               
                return JsonResponse({"message": "Error", "errors": form.errors}, status=400)

        if request.method =="GET":
            aticleForm =  ArticleForm()
            return render(request,'back/addarticle.html',{'form':aticleForm})
    else:
        return render(request,"back/addarticle.html")
##
# Method to add new notice.
#     
def addNotice(request):
    if request.user.is_authenticated:
        NoticeImageFormSet = modelformset_factory(
                                    NoticeImages, form=NoticeImageForm, extra=1, can_delete=True
                                     )
        NoticeDocumentFormSet = modelformset_factory(
                                    NoticeDocuments, form=NoticeDocumentForm, extra=1, can_delete=True
                                    )

        if request.method =="POST":
            form = NoticeForm(request.POST,request.FILES)
            notice_image_formset = NoticeImageFormSet(request.POST or None, request.FILES or None)
            notice_document_formset = NoticeDocumentFormSet(request.POST or None,request.FILES or None)
            if form.is_valid() and notice_image_formset.is_valid() and notice_document_formset.is_valid():
                ##Save the form
                notice_instance = form.save(commit=False)
                notice_instance.owner = request.user
                notice_instance.save()
                images_instances = notice_image_formset.save(commit=False)
                document_instances = notice_document_formset.save(commit=False)

                ## As actual formset is not used, make a placeholder
                if not images_instances:
                    images_instances = [NoticeImages()]
                    

                if not document_instances:
                    document_instances = [NoticeDocuments()]
                  

                for idx, image in enumerate(images_instances):
                    image_files = request.FILES.getlist(f'image_{idx+1}')  
                    for image_file in image_files:
                        # Create a new image object for each uploaded file
                        notice_image = NoticeImages.objects.create(
                            image=image_file,
                            notice=notice_instance,
                            owner = request.user
                            
                        )
                        notice_image.save()
                         
                    for idx, documents in enumerate(document_instances):
                        docs = request.FILES.getlist(f'files_{idx+1}')
                        for doc in docs:
                            notice_docs = NoticeDocuments.objects.create(
                                notice = notice_instance,
                                document = doc,
                                owner = request.user
                            )
                            notice_docs.save()
                return JsonResponse({"status":"Success","message":f"Notice :{notice_instance.title} Saved!!"},status=200)
            else:
                
                    all_errors ={}
                    all_errors["form errors"] = form.errors.as_json
                    all_errors["notice_image_errors"] = [
                        form.errors.as_json() for form in notice_image_formset.forms if form.errors
                    ]
                    all_errors["notice_documents_errors"] =[
                        form.errors.as_json() for form in notice_document_formset.forms if form.errors
                    ]
                    return JsonResponse({"status":"fail","message":f"Notice :{notice_instance.noticeTitle} Could not be published!!"})

        if request.method =="GET":
            noticeForm =  NoticeForm()
            notice_image_formset = NoticeImageFormSet(queryset=NoticeImages.objects.none())
            notice_document_formset = NoticeDocumentFormSet(queryset=NoticeDocuments.objects.none())
            return render(request,'back/addnotice.html',{
                'form':noticeForm,
                'image_formset':notice_image_formset,
                'document_Formset':notice_document_formset})
    else:
        return redirect('login')
    

def addMessage(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form = MessageForm(request.POST,request.FILES)
            if form.is_valid():
                messagef = form.save(commit=False)
                messagef.owner  = request.user
                messagef.save()
                return JsonResponse({'status':'success','message':'Message added successfully!!'},status=200)
            else:
                return JsonResponse({'status':'fail','message':'Could not publish  message','error':form.errors},status=400)
        else:
            form = MessageForm()
            return render(request,"back/addMessage.html", {"form":form})
    else:
        return redirect('login')



def createUser(request):
    return render(request,"back/register.html")



  


