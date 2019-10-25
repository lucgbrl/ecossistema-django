#project base url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    url(r'ˆjet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include('materiais.urls')),
]
