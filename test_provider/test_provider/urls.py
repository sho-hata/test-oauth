
from django.contrib import admin
from django.urls import path, include
from .views import profile_view, top_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', top_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/profile/', profile_view, name='profile'),
]
