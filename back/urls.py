from django.urls import path
from . import views
urlpatterns =[
    path('newmenu/',views.addMenu,name="newmenu")
]