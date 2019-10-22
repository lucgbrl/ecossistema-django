from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name = "index"),
    path('material/', views.lista, name = "material"),  
    path('detalhes/<int:pk>/', views.detalhes, name="detalhes"),  
    path('new/', views.new, name="new"),
    path('usuarios/', views.usuarios, name='usuarios'),
    #path('material/new/', views.post_new, name = 'post_new'),
    #path('material/detalhes/', views.detalhes, name='detalhes'),
]
