from django.db import models


class GalleryCategory(models.Model):
    name = models.CharField("Nombre", max_length=100)
    slug = models.SlugField("Slug", unique=True)
    order = models.IntegerField("Orden", default=0)

    class Meta:
        verbose_name = "Categoría de galería"
        verbose_name_plural = "Categorías de galería"
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    title = models.CharField("Título", max_length=200, blank=True)
    description = models.TextField("Descripción", blank=True)
    image = models.ImageField("Imagen", upload_to="gallery/")
    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Categoría",
        related_name="images",
    )
    published = models.BooleanField("Publicado", default=True, db_index=True)
    order = models.IntegerField("Orden", default=999, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Imagen de galería"
        verbose_name_plural = "Imágenes de galería"
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title or f"Imagen {self.id}"
