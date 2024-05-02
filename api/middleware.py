from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        
        print(request.user)
        if not request.path == '/api/login/':
            if not request.user.is_authenticated:
                response = Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
                
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = "application/json"
                response.renderer_context = {}
                response.render()
                
                return response
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    
