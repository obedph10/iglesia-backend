from django.db import models


class Series(models.Model):
    name = models.CharField("Nombre", max_length=200)
    description = models.TextField("Descripción", blank=True)
    image = models.ImageField("Imagen", upload_to="series/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Serie"
        verbose_name_plural = "Series"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Sermon(models.Model):
    title = models.CharField("Título", max_length=300)
    description = models.TextField("Descripción", blank=True)
    speaker = models.CharField("Predicador", max_length=200)
    youtube_url = models.URLField("URL de YouTube")
    date = models.DateField("Fecha")
    image = models.ImageField("Imagen", upload_to="sermons/", blank=True)
    series = models.ForeignKey(
        Series,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Serie",
        related_name="sermons",
    )
    published = models.BooleanField("Publicado", default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Predicación"
        verbose_name_plural = "Predicaciones"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.title} - {self.speaker}"
