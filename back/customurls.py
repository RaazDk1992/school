from django.urls import path
from django.utils.module_loading import import_string
from back.models import Menu
import traceback

def dynamicPaths():
    url_patterns = []
    
    try:
        menus = Menu.objects.all()
        for route in menus:
            try:
                view = import_string("back.views.dynamicView")  # Ensure correct module path
                url_patterns.append(path(route.menuPath + '/', view))  # Add trailing slash
            except ImportError as e:
                print(f"Error importing view for route {route.menuPath}: {e}")
                traceback.print_exc()  # Print full error traceback
    except Exception as e:
        print(f"Database error fetching menu items: {e}")
        traceback.print_exc()
    
    print("Dynamic URLs added:", url_patterns)
    return url_patterns

# Ensure calling the function returns the list of patterns
dynamic_patterns = lambda: dynamicPaths()
