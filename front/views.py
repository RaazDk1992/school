from django.http import HttpResponse
from django.shortcuts import render
from back.models import Sliders,Message

def index(request):
    sliders = Sliders.objects.filter(is_active=True)
    messages = Message.objects.filter(is_active = True)
    print(sliders)
    context = {
        'sliders': sliders,
        'messages': messages
    }
    return render(request,"front\\index.html",context)
def say_x(request):
    return render(request,"front\\index.html")

