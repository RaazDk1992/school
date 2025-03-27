from back.models import Menu,Testimonials

def navbar_items(request):
    items = Menu.objects.all()

    
    for item in items:
        if not item.menuPath.startswith('/'):
            item.menuPath = '/' + item.menuPath  

    return {"navbar_items": items}  

def load_testimonials(request):
    items = Testimonials.objects.all()
    return {"testimonials":items}

def breadcrumbs(request):
    path_parts = [part for part in request.path.strip('/').split('/') if part]
    breadcrumb_links = []
    current_path = ""

    for part in path_parts:
        current_path += f"/{part}"
        breadcrumb_links.append({"name": part.capitalize(), "url": current_path})

    return {"breadcrumbs": breadcrumb_links}

