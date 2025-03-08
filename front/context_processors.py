from back.models import Menu

def navbar_items(request):
    items = Menu.objects.all() 
    return {"navbar_items": items}
