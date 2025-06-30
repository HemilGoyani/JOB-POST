from django.contrib import admin
from django.urls import path, include
from .views import *
from users.views import login_view, register
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name="dashboard"),
    path('', login_view, name="login"),
    path('registeration/', register, name="registeration"),
    path('users/', include('users.urls')),
    path('jobs/', include('jobs.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

