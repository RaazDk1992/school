from django.urls import path,re_path
from . import views
urlpatterns =[
    path('login/',views.userLogin,name="login"),
    path("createuser/",views.createUser, name="createuser"),
    path('newmenu/',views.addMenu,name="newmenu"),
    path('bye/',views.sayBye,name="bye"),
    path('newcontentType/',views.addContentType,name="addcontenttype")
]