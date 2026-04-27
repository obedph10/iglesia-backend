from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField("Título", max_length=200)
    slug = models.SlugField("Slug", unique=True)
    content = RichTextField("Contenido")
    meta_description = models.TextField("Meta descripción", blank=True)
    published = models.BooleanField("Publicado", default=True)
    order = models.IntegerField("Orden", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ["order", "title"]

    def __str__(self):
        return self.title
