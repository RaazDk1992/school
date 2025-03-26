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
    path("edit_gallery/<int:gallery_id>", views.edit_gallery, name="edit_gallery"),
    path("edit_dyanmic/<int:id>",views.editDynamic,name="edit_dynamic"),
    path("delete-dynamic/<int:id>",views.deleteDynamic,name="delete-dynamic"),
    path("delete-notice/<int:id>",views.deleteNotice,name="delete-notice"),
    path("delete-event/<int:id>",views.deleteEvent,name="delete-notice"),
    path("delete-gallery/<int:id>",views.deleteGallery,name="delete-gallery"),
    path('newgallery',views.addGallery,name="newgallery"),
    path('addmessage/',views.addMessage,name="newmessage"),
    path('addtestimonial',views.addTestimonial,name="addtestimonial"),
    path('addslider/',views.addSlider,name="addslider"),
    path('addevents/',views.addEvents,name="addevents"),
    path('addmenu/',views.addMenu,name="addmenu"),
    path('addcontenttype/',views.addContentType,name="addcontenttype"),
    path('content/create/',views.createContent,name="createcontent"),
    path('bye/',views.sayBye,name="bye"),
]
urlpatterns.extend(dynamicPaths())
