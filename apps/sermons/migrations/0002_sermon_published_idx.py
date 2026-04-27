from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sermons", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sermon",
            name="published",
            field=models.BooleanField(default=True, verbose_name="Publicado", db_index=True),
        ),
    ]
