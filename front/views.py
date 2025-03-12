from django.http import HttpResponse
from django.shortcuts import render
from back.models import Sliders,Message,Notices,Gallery,Image
from django.db.models import Prefetch

def index(request):
    sliders = Sliders.objects.filter(is_active=True)
    messages = Message.objects.filter(is_active = True)
    context = {
        'sliders': sliders,
        'messages': messages
    }
    return render(request,"front\\index.html",context)
def loadNotices(request):
    notices = Notices.objects.all()
    context={
        'viewName':'Notices',
        'list':notices
    }
    return render(request,"front\\listview.html",context)

def showGalleries(request):
   
    galleries = Gallery.objects.prefetch_related(
        Prefetch('image_set', queryset=Image.objects.all())
    ).order_by('-creation_date')
    
    return render(request, 'front/timeline.html',{'galleries':galleries})


