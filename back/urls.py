from django.urls import path,re_path
from . import views
urlpatterns =[
    path('login/',views.userLogin,name="login"),
    path("createuser/",views.createUser, name="createuser"),
    path('dashboard/',views.loadDashboard,name="dashboard"),
    path('newarticle/',views.addArticle,name="newArticle"),
    path('newnotice/',views.addNotice,name="addnotice"),
    path('newgallery',views.addGallery,name="newgallery"),
    path('addmessage/',views.addMessage,name="newmessage"),
    path('addslider/',views.addSlider,name="addslider"),
    path('addmenu/',views.addMenu,name="addmenu"),
    path("timeline/",views.showTimeLine, name="timeline"),
    path('content/create/',views.createContent,name="createcontent"),
    path('content/<slug:slug>/',views.renderDynamic,name="renderdynamic"),

    path('bye/',views.sayBye,name="bye"),
]