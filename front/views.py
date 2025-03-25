from django.http import HttpResponse, Http404
from django.shortcuts import render,get_object_or_404
from back.models import Sliders,Message,Notices,Gallery,Image,Events,Menu,ContentType,Dynamic
from django.db.models import Prefetch

def index(request):
    sliders = Sliders.objects.filter(is_active=True)
    messages = Message.objects.filter(is_active = True)
    events = Events.objects.all()
    notices = Notices.objects.all()
    context = {
        'sliders': sliders,
        'messages': messages,
        'events':events,
        'notices':notices
    }
    return render(request,"front\\index.html",context)

def loadNotices(request):
    notices = Notices.objects.all()
    context={
        'viewName':'Notices',
        'list':notices,
        'base':'noticedetails'
    }
    return render(request,"front\\listview.html",context)


def noticeDetails(request,noticeId):
    notice = get_object_or_404(Notices.objects.prefetch_related('noticeimages_set', 'noticedocuments_set'), id=noticeId)
    return render(request,'front/detailed1.html',{'content':notice})

def dynamicView(request):

    #strip slashesh to get actual menu items.
    path = request.path.strip('/').split('/')[-1]
   
    try:
        menu = Menu.objects.get(menuItem=path)
        contentTypeRef = get_object_or_404(ContentType, id=menu.contentType_id)
        contents = Dynamic.objects.filter(contentType=contentTypeRef)
        return render(request,'front/listview.html',{'list':contents,'viewName':menu,'base':'detail'})
    except Menu.DoesNotExist:
        raise Http404("Menu item does not exist")
   


def loadDynamicContent(request, contentId):
    content = Dynamic.objects.get(id=contentId)
    return render(request,'front/detailed.html',{'content':content})

def showGalleries(request):
   
    galleries = Gallery.objects.prefetch_related(
        Prefetch('image_set', queryset=Image.objects.all())
    ).order_by('-creation_date')
    
    return render(request, 'front/timeline.html',{'galleries':galleries})


def show404(request):
    return render(request,'404.html')


