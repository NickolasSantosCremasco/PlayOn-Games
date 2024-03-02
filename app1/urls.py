
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='inicial'),
    path('games', views.games, name='games'),
    path('sobre', views.about, name='about'),
    path('contato', views.contact, name='contact'),
    path('criação', views.creation, name='creation')
]
