from django.contrib import admin
from django.urls import path
from base import views as base_views
from django.conf.urls.static import static
from portfolio import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_views.home)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
