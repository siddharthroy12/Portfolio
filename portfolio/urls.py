from django.contrib import admin
from django.urls import path, include
from base import views as base_views
from django.conf.urls.static import static
from portfolio import settings
from projects.views import projects_view
from blog.views import blogs_view, blog_view

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('projects/', projects_view, name='projects'),
    path('blog/<int:id>/',blog_view, name='blog'),
    path('blog/', blogs_view, name='blogs'),
    path('', base_views.home)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
