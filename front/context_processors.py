from back.models import Menu

def navbar_items(request):
    items = Menu.objects.all()

    
    for item in items:
        if not item.menuPath.startswith('/'):
            item.menuPath = '/' + item.menuPath  

    return {"navbar_items": items}  

