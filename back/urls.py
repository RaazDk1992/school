from django.urls import path,re_path,include
from back.customurls import dynamicPaths
from . import views
urlpatterns =[
    path('login/',views.userLogin,name="login"),
    path("createuser/",views.createUser, name="createuser"),
    path('dashboard/',views.loadDashboard,name="dashboard"),
    path('newarticle/',views.addArticle,name="newArticle"),
    path('newnotice/',views.addNotice,name="addnotice"),
    path('edit-notice/<int:notice_id>/', views.editNotice, name='edit_notice'),
    path('newgallery',views.addGallery,name="newgallery"),
    path('addmessage/',views.addMessage,name="newmessage"),
    path('addslider/',views.addSlider,name="addslider"),
    path('addmenu/',views.addMenu,name="addmenu"),
    path('addcontenttype/',views.addContentType,name="addcontenttype"),
    path('content/create/',views.createContent,name="createcontent"),
    path('bye/',views.sayBye,name="bye"),
]
urlpatterns.extend(dynamicPaths())
