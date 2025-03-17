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

