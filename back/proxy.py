import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
def proxy_view(request,path):
    BACKEND_URL = "http://127.0.0.1:8000/back/" 
    target_url = f"{BACKEND_URL}{path}"
    try:
        if request.method == "GET":
            response = requests.get(target_url, params=request.GET)
        elif request.method == "POST":
            response = requests.post(target_url,data=request.POST)

        else:
            return JsonResponse({"error": "Method not allowed"}, status=405)
        return JsonResponse(response.json(), safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)

def  proxy_view_with_render(request,path):
    BACKEND_URL = "http://127.0.0.1:8000/back/"
    headerx = {"X-CSRFToken": request.META.get("CSRF_COOKIE")}  

    target_url = f"{BACKEND_URL}{path}"
    if request.method == "GET":
        response = requests.get(target_url,params=request.GET,headers=headerx)
        if response.status_code ==200:
            return render(request,'back/login.html')
