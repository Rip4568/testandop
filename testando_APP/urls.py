from .views import pagina1,pagina2
from django.urls import path

urlpatterns = [
    path('',pagina1),
    path('home',pagina2),
]
