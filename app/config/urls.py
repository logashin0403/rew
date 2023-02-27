from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('src.users.urls')),
    path('news/', include('src.news.urls')),
    path('info/', include('src.userinfo.urls')),
    path('maps/', include('src.maps.urls')),
]
