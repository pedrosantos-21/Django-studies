from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('painel/', admin.site.urls),
    path('', include('core.urls')), #Recomenadado criar um URLS.py para cada app
]
