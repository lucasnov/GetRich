from django.urls import path

from . import views

urlpatterns = [
    path('api/money/<str:moedas>/', views.getCotacao),
    path('api/favs/', views.getFav),
    path('api/comps/', views.getComp),
    path('api/fav/', views.setConfig),
    path('api/comp/', views.setConfig),
    # Você possivelmente tem outras rotas aqui.
]