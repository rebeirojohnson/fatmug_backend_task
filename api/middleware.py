from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.conf import settings

class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        is_authenticated = request.session.get('is_authenticated',False)
               
        if not is_authenticated and not request.path == settings.LOGIN_URL:
            
            response = Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
            
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            response.render()
            
            return response

        response = self.get_response(request)

        return response
    
