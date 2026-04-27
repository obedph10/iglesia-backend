from django.db import models
from ckeditor.fields import RichTextField


class Alliance(models.Model):
    name = models.CharField("Nombre de la alianza", max_length=300)
    description = RichTextField("Descripción")
    logo = models.ImageField("Logo", upload_to="alliances/", blank=True)
    website = models.URLField("Sitio web", blank=True)
    is_active = models.BooleanField("Activo", default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Alianza"
        verbose_name_plural = "Alianzas"
        ordering = ["name"]

    def __str__(self):
        return self.name


class AllianceProject(models.Model):
    IMPACT_CATEGORIES = [
        ("educacion", "Educación"),
        ("alimentacion", "Alimentación"),
        ("vivienda", "Vivienda"),
        ("salud", "Salud"),
        ("deporte", "Deporte y Recreación"),
        ("arte", "Arte y Cultura"),
        ("ambiente", "Medio Ambiente"),
        ("emprendimiento", "Emprendimiento"),
        ("otro", "Otro"),
    ]

    alliance = models.ForeignKey(
        Alliance,
        on_delete=models.CASCADE,
        verbose_name="Alianza",
        related_name="projects",
    )
    title = models.CharField("Título del proyecto", max_length=300)
    description = RichTextField("Descripción")
    image = models.ImageField("Imagen", upload_to="alliance_projects/", blank=True)
    impact_category = models.CharField(
        "Categoría de impacto", max_length=20, choices=IMPACT_CATEGORIES, default="otro", db_index=True
    )
    start_date = models.DateField("Fecha de inicio")
    end_date = models.DateField("Fecha de fin", blank=True, null=True)
    location = models.CharField("Ubicación", max_length=300, blank=True)
    volunteers_needed = models.IntegerField("Voluntarios necesitados", default=0)
    is_active = models.BooleanField("Activo", default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Proyecto de alianza"
        verbose_name_plural = "Proyectos de alianzas"
        ordering = ["-start_date"]

    def __str__(self):
        return self.title
