from django.shortcuts import redirect
from django.urls import resolve, Resolver404

class RedirectInvalidUrlsMiddleware:
    """
    Middleware para redirecionar URLs inválidas para a página inicial.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            # Verifica se a URL é válida
            resolve(request.path)
        except Resolver404:
            # Redireciona para a página inicial se a URL for inválida
            return redirect('home')

        response = self.get_response(request)
        return response