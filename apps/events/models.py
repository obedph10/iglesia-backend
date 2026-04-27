from django.db import models


class Event(models.Model):
    CATEGORY_CHOICES = [
        ("culto", "Culto"),
        ("especial", "Evento Especial"),
        ("jovenes", "Jóvenes"),
        ("ninos", "Niños"),
        ("comunitario", "Comunitario"),
        ("otro", "Otro"),
    ]

    title = models.CharField("Título", max_length=300)
    description = models.TextField("Descripción", blank=True)
    date = models.DateField("Fecha")
    time = models.TimeField("Hora", blank=True, null=True)
    end_date = models.DateField("Fecha fin", blank=True, null=True)
    location = models.CharField("Ubicación", max_length=300, blank=True)
    image = models.ImageField("Imagen", upload_to="events/", blank=True)
    category = models.CharField(
        "Categoría", max_length=20, choices=CATEGORY_CHOICES, default="culto"
    )
    registration_link = models.URLField("Enlace de registro", blank=True)
    published = models.BooleanField("Publicado", default=True)
    featured = models.BooleanField("Destacado", default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["date", "time"]

    def __str__(self):
        return self.title
