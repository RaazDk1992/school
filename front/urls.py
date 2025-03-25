from django.urls import path,include
from front.customurls import dynamicPaths,dynamic_patterns
from . import views
urlpatterns =[
    
    path('',views.index,name="index"),
    path('notices/',views.loadNotices,name="notices"),
    path('gallery/',views.showGalleries,name="gallery"),
    path('detail/<int:contentId>/',views.loadDynamicContent,name="load_dynamic_content"),
]

urlpatterns +=dynamicPaths()

