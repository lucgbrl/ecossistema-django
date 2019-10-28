#project base url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

#from django.contrib.auth import views as  auth_views

urlpatterns = [
    path('', include('materiais.urls')),
    url(r'ˆjet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    #path('login/', include('login.urls')),s
    path('login/', include('django.contrib.auth.urls')),
    #path('logout/', auth_views.LogoutView.as_view(), name="logouts"),
    
]
