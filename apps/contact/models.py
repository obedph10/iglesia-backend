from django.db import models


class ContactMessage(models.Model):
    name = models.CharField("Nombre", max_length=200)
    email = models.EmailField("Email")
    phone = models.CharField("Teléfono", max_length=50, blank=True)
    subject = models.CharField("Asunto", max_length=300)
    message = models.TextField("Mensaje")
    is_read = models.BooleanField("Leído", default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mensaje de contacto"
        verbose_name_plural = "Mensajes de contacto"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"


class PrayerRequest(models.Model):
    name = models.CharField("Nombre", max_length=200, blank=True)
    email = models.EmailField("Email", blank=True)
    prayer_request = models.TextField("Petición de oración")
    is_private = models.BooleanField("Privado", default=True)
    is_answered = models.BooleanField("Respondido", default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Petición de oración"
        verbose_name_plural = "Peticiones de oración"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name or f"Anónimo - {self.created_at.strftime('%d/%m/%Y')}"


class SiteSettings(models.Model):
    address = models.CharField("Dirección", max_length=255)
    phone = models.CharField("Teléfono", max_length=50, blank=True)
    email = models.EmailField("Email de la iglesia", blank=True)
    google_maps_url = models.URLField("URL de Google Maps", blank=True)
    schedule = models.TextField("Horarios de cultos", blank=True)
    mission = models.TextField("Misión", blank=True)
    vision = models.TextField("Visión", blank=True)
    about_us = models.TextField("Sobre nosotros (Nuestra Historia)", blank=True)
    our_faith = models.TextField("Nuestra Fe", blank=True)
    faith_declaration = models.TextField("Nuestra Declaración de Fe", blank=True)
    
    # Home Page
    home_title = models.CharField("Título de Inicio", max_length=255, blank=True)
    home_subtitle = models.TextField("Subtítulo de Inicio", blank=True)
    home_pillar_1_title = models.CharField("Pilar 1 (Título)", max_length=100, blank=True)
    home_pillar_1_desc = models.TextField("Pilar 1 (Descripción)", blank=True)
    home_pillar_2_title = models.CharField("Pilar 2 (Título)", max_length=100, blank=True)
    home_pillar_2_desc = models.TextField("Pilar 2 (Descripción)", blank=True)
    home_pillar_3_title = models.CharField("Pilar 3 (Título)", max_length=100, blank=True)
    home_pillar_3_desc = models.TextField("Pilar 3 (Descripción)", blank=True)
    home_pillar_4_title = models.CharField("Pilar 4 (Título)", max_length=100, blank=True)
    home_pillar_4_desc = models.TextField("Pilar 4 (Descripción)", blank=True)

    # Donations
    donations_bible_verse = models.TextField("Versículo (Donaciones)", blank=True)
    donations_bible_reference = models.CharField("Referencia (Donaciones)", max_length=100, blank=True)
    donations_why_donate = models.TextField("¿Por qué donar?", blank=True)

    # Socials
    facebook_url = models.URLField("Facebook", blank=True)
    instagram_url = models.URLField("Instagram", blank=True)
    youtube_url = models.URLField("YouTube", blank=True)
    tiktok_url = models.URLField("TikTok", blank=True)

    class Meta:
        verbose_name = "Configuración del sitio"
        verbose_name_plural = "Configuración del sitio"

    def __str__(self):
        return "Configuración del sitio"
