from django.urls import path
from . import views
urlpatterns =[
    path('',views.say_hi,name="hi"),
    path('notices/',views.say_x,name="x"),
]
