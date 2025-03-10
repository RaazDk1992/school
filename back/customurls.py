
from django.urls import path
from django.utils.module_loading import import_string
from back.models import Menu

def dynamicPaths():
    url_patterns = []
    for route in Menu.objects.all():
        try:
            view = import_string("dynamicView")
            url_patterns.append(path(route.menuPath,view))
        except ImportError:
            pass
    return url_patterns
dynamic_patterns = lambda:dynamicPaths