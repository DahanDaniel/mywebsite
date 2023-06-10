from django.contrib import admin
from .models import Gallery, Image

# admin.site.register(Gallery)
# admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  # How many rows to show


class GalleryAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)


admin.site.register(Gallery, GalleryAdmin)
