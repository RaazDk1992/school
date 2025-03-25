from django.http import HttpResponse
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
        'list':notices
    }
    return render(request,"front\\listview.html",context)


def dynamicView(request):

    #strip slashesh to get actual menu items.
    path = request.path.strip('/').split('/')[-1]
    #get contentType from menu,  we are getting menu object with menu itemname = path, then getting its conttenttpe ref from there.
    contentTypeRef =get_object_or_404(ContentType, id=Menu.objects.get(menuItem=path).contentType_id)
    #get the list of items of that particular type.
    contents = Dynamic.objects.filter(contentType=contentTypeRef)
    return render(request,'front/dynamic.html',{'list':contents})


def loadDynamicContent(request, contentId):
    content = Dynamic.objects.get(id=contentId)
    return render(request,'front/detailed.html',{'content':content})

def showGalleries(request):
   
    galleries = Gallery.objects.prefetch_related(
        Prefetch('image_set', queryset=Image.objects.all())
    ).order_by('-creation_date')
    
    return render(request, 'front/timeline.html',{'galleries':galleries})


