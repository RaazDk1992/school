from django.urls import clear_url_caches, get_resolver
from django.conf import settings
from back.customurls import dynamicPaths  

class DynamicURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.reload_dynamic_urls()
        response = self.get_response(request)
        return response

    def reload_dynamic_urls(self):
        """Reloads URLs dynamically from the database."""
        clear_url_caches()  # Clear Django’s URL cache
        settings.ROOT_URLCONF = settings.ROOT_URLCONF  # Force URL reload
        get_resolver().url_patterns += dynamicPaths()  # Append fresh patterns
