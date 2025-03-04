from django.urls import path,re_path
from . import views
urlpatterns =[
    path('login/',views.userLogin,name="login"),
    path("createuser/",views.createUser, name="createuser"),
    path('dashboard/',views.loadDashboard,name="dashboard"),
    path('newarticle/',views.addArticle,name="newArticle"),
    path('bye/',views.sayBye,name="bye"),
]