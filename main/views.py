from django.shortcuts import render, get_object_or_404
from .models import Gallery


def gallery_detail(request, title):
    gallery = get_object_or_404(Gallery, title=title)
    for image in gallery.images.all():
        print(image.image.url)
    return render(request, "main/gallery_detail.html", {"gallery": gallery})


def home(request):
    return render(request, "main/home.html")


def blog(request):
    return render(request, "main/blog.html")


def gallery(request):
    galleries = Gallery.objects.all()
    return render(request, "main/gallery.html", {"galleries": galleries})


def social(request):
    return render(request, "main/social.html")


def contact(request):
    return render(request, "main/contact.html")


def about(request):
    return render(request, "main/about.html")
