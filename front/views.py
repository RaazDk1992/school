from django.http import HttpResponse
from django.shortcuts import render
from back.models import Sliders,Message,Notices,Gallery,Image,Events
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

    path = request.path.rstrip('/').split('/')[-1] 
    print(request.path)
    return render(request,'back/login.html')

def showGalleries(request):
   
    galleries = Gallery.objects.prefetch_related(
        Prefetch('image_set', queryset=Image.objects.all())
    ).order_by('-creation_date')
    
    return render(request, 'front/timeline.html',{'galleries':galleries})


