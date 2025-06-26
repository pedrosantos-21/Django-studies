from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('painel/', admin.site.urls),
    path('', include('core.urls')), #Recomenadado criar um URLS.py para cada app
]

handler404 = views.error404
handler500 = views.error500
