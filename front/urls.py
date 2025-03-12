from django.urls import path
from front.customurls import dynamicPaths
from . import views
urlpatterns =[
    path('',views.index,name="index"),
    path('notices/',views.loadNotices,name="notices"),
    path('gallery/',views.showGalleries,name="gallery"),
]

urlpatterns.extend(dynamicPaths())

