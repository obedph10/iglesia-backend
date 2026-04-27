from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alliances", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alliance",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Activo", db_index=True),
        ),
        migrations.AlterField(
            model_name="allianceproject",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Activo", db_index=True),
        ),
        migrations.AlterField(
            model_name="allianceproject",
            name="impact_category",
            field=models.CharField(
                choices=[
                    ("educacion", "Educación"),
                    ("alimentacion", "Alimentación"),
                    ("vivienda", "Vivienda"),
                    ("salud", "Salud"),
                    ("deporte", "Deporte y Recreación"),
                    ("arte", "Arte y Cultura"),
                    ("ambiente", "Medio Ambiente"),
                    ("emprendimiento", "Emprendimiento"),
                    ("otro", "Otro"),
                ],
                db_index=True,
                default="otro",
                max_length=20,
                verbose_name="Categoría de impacto",
            ),
        ),
    ]
