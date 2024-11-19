from django.contrib import admin
from django.urls import path, include
from core import views  # Importando as views do 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Definir a home como a página principal, é definido quando a rota fica vazia ""
    path('', include('core.urls')),

    # URL para acessar a página de login
    path('servicos/', views.servicos, name="servicos"),
    
    # Incluir todas as URLs do app 'core'
]