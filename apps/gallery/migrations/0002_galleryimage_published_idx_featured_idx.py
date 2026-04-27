from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="galleryimage",
            name="published",
            field=models.BooleanField(default=True, verbose_name="Publicado", db_index=True),
        ),
        migrations.AlterField(
            model_name="galleryimage",
            name="featured",
            field=models.BooleanField(default=False, verbose_name="Destacado", db_index=True),
        ),
    ]
