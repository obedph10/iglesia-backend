from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from apps.contact.models import SiteSettings


class Command(BaseCommand):
    help = 'Setup initial SiteSettings data from environment variables or defaults'

    def add_arguments(self, parser):
        parser.add_argument(
            '--use-env',
            action='store_true',
            help='Read values from environment variables',
        )

    def handle(self, *args, **options):
        settings_obj, created = SiteSettings.objects.get_or_create(id=1)

        if options['use_env']:
            # Read from environment (for production deploys)
            settings_obj.address = self.get_env('CHURCH_ADDRESS', settings_obj.address)
            settings_obj.email = self.get_env('CHURCH_EMAIL', settings_obj.email)
            settings_obj.phone = self.get_env('CHURCH_PHONE', settings_obj.phone)
            settings_obj.schedule = self.get_env('CHURCH_SCHEDULE', settings_obj.schedule)
            settings_obj.google_maps_url = self.get_env('CHURCH_MAPS_URL', settings_obj.google_maps_url)
            settings_obj.facebook_url = self.get_env('CHURCH_FACEBOOK', settings_obj.facebook_url)
            settings_obj.instagram_url = self.get_env('CHURCH_INSTAGRAM', settings_obj.instagram_url)
            settings_obj.youtube_url = self.get_env('CHURCH_YOUTUBE', settings_obj.youtube_url)
            settings_obj.tiktok_url = self.get_env('CHURCH_TIKTOK', settings_obj.tiktok_url)
            message = "SiteSettings populated from environment variables"
        else:
            # Interactive prompt (for local development)
            self.stdout.write(self.style.SUCCESS('Setup SiteSettings (press Enter to skip)\n'))

            settings_obj.address = self.prompt('Address', settings_obj.address)
            settings_obj.email = self.prompt('Email', settings_obj.email)
            settings_obj.phone = self.prompt('Phone', settings_obj.phone)
            settings_obj.schedule = self.prompt('Service Schedule', settings_obj.schedule)
            settings_obj.google_maps_url = self.prompt('Google Maps URL', settings_obj.google_maps_url)
            settings_obj.facebook_url = self.prompt('Facebook URL', settings_obj.facebook_url)
            settings_obj.instagram_url = self.prompt('Instagram URL', settings_obj.instagram_url)
            settings_obj.youtube_url = self.prompt('YouTube URL', settings_obj.youtube_url)
            settings_obj.tiktok_url = self.prompt('TikTok URL', settings_obj.tiktok_url)
            message = "SiteSettings updated interactively"

        settings_obj.save()
        self.stdout.write(self.style.SUCCESS(f'✓ {message}\n'))
        self.stdout.write(self.style.WARNING('Note: Changes may take up to 60s to appear due to Redis cache'))

    @staticmethod
    def get_env(key, default=''):
        import os
        return os.getenv(key, default)

    @staticmethod
    def prompt(label, current_value=''):
        prompt_text = f'{label}'
        if current_value:
            prompt_text += f' [{current_value}]'
        prompt_text += ': '
        value = input(prompt_text).strip()
        return value if value else current_value
