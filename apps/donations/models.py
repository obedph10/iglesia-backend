from django.db import models


class DonationOption(models.Model):
    METHOD_CHOICES = [
        ("paypal", "PayPal"),
        ("bank_transfer", "Transferencia Bancaria"),
        ("card", "Tarjeta de Crédito/Débito"),
        ("other", "Otro"),
    ]

    payment_method = models.CharField(
        "Método de pago", max_length=20, choices=METHOD_CHOICES
    )
    label = models.CharField("Etiqueta", max_length=100)
    description = models.TextField("Descripción", blank=True)

    # Bank transfer fields
    bank_name = models.CharField("Nombre del banco", max_length=200, blank=True)
    account_type = models.CharField("Tipo de cuenta", max_length=50, blank=True)
    account_number = models.CharField("Número de cuenta", max_length=100, blank=True)
    account_holder = models.CharField("Titular", max_length=200, blank=True)
    identification = models.CharField("Identificación", max_length=50, blank=True)

    # PayPal
    paypal_email = models.EmailField("Email de PayPal", blank=True)

    # Card
    card_image = models.ImageField(
        "Imagen de tarjeta", upload_to="donations/", blank=True
    )

    is_active = models.BooleanField("Activo", default=True)
    order = models.IntegerField("Orden", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Opción de donación"
        verbose_name_plural = "Opciones de donación"
        ordering = ["order"]

    def __str__(self):
        return self.label


class Donation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pendiente"),
        ("completed", "Completado"),
        ("failed", "Fallido"),
    ]

    amount = models.DecimalField("Monto", max_digits=12, decimal_places=2)
    donor_name = models.CharField("Nombre del donante", max_length=200, blank=True)
    donor_email = models.EmailField("Email del donante", blank=True)
    payment_method = models.CharField("Método de pago", max_length=20)
    transaction_id = models.CharField(
        "ID de transacción", max_length=200, blank=True, unique=True
    )
    status = models.CharField(
        "Estado", max_length=20, choices=STATUS_CHOICES, default="pending"
    )
    message = models.TextField("Mensaje", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Donación"
        verbose_name_plural = "Donaciones"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.donor_name or 'Anónimo'} - ${self.amount}"
