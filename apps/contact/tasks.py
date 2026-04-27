from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def send_contact_emails(self, contact_data: dict, church_email: str):
    try:
        send_mail(
            subject=f"Nuevo mensaje de contacto: {contact_data.get('subject')}",
            message=(
                f"Nuevo mensaje de contacto:\n\n"
                f"Nombre: {contact_data.get('name')}\n"
                f"Email: {contact_data.get('email')}\n"
                f"Teléfono: {contact_data.get('phone') or 'No proporcionado'}\n"
                f"Asunto: {contact_data.get('subject')}\n\n"
                f"Mensaje:\n{contact_data.get('message')}\n\n"
                f"---\nEste mensaje fue enviado a través del formulario de contacto en tu sitio web."
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[church_email],
            fail_silently=False,
        )
    except Exception as exc:
        raise self.retry(exc=exc)

    try:
        send_mail(
            subject="Hemos recibido tu mensaje - Iglesia Cristiana La Roca",
            message=(
                f"Hola {contact_data.get('name')},\n\n"
                f"Gracias por contactarnos. Hemos recibido tu mensaje y pronto nos pondremos en contacto contigo.\n\n"
                f"Detalles de tu mensaje:\n"
                f"Asunto: {contact_data.get('subject')}\n\n"
                f"Si tienes alguna pregunta urgente, no dudes en llamarnos o visitarnos.\n\n"
                f"¡Que Dios te bendiga!\n\n---\nIglesia Cristiana La Roca"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[contact_data.get("email")],
            fail_silently=True,
        )
    except Exception:
        pass
