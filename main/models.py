from django.db import models
from django.utils.text import slugify
import os


def get_upload_image_to(instance, filename):
    title = instance.gallery.title
    return os.path.join("galleries", f"{title}", filename)


class Image(models.Model):
    image = models.ImageField(upload_to=get_upload_image_to)
    gallery = models.ForeignKey(
        "Gallery", related_name="images", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.description if self.description else self.image.name


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(
        upload_to="galleries/covers", blank=True, null=True
    )

    def __str__(self):
        return self.title
