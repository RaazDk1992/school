from django.http import HttpResponse
from django.shortcuts import render

def say_hi(request):
    return render(request,"front\\index.html")
def say_x(request):
    return render(request,"front\\index.html")

