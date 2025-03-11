from django.urls import path
from front.customurls import dynamicPaths
from . import views
urlpatterns =[
    path('',views.index,name="index"),
    path('notices/',views.say_x,name="x"),
]

urlpatterns.extend(dynamicPaths())

