from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("gallery/", views.gallery, name="gallery"),
    path("gallery/<str:title>/", views.gallery_detail, name="gallery_detail"),
    path("blog/", views.blog, name="blog"),
    path("social/", views.social, name="social"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]

if settings.DEBUG:  # In development, serve media files through Django.
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
