# Generated by Django 4.2.2 on 2023-06-15 13:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ai_tools", "0006_alter_aitool_april_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aitool",
            name="april",
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="average_time_normalized",
            field=models.DecimalField(
                decimal_places=3,
                max_digits=5,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="average_time_on_website",
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="change_normalized",
            field=models.DecimalField(
                decimal_places=3,
                max_digits=5,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="engagement",
            field=models.DecimalField(
                decimal_places=3,
                max_digits=5,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="february",
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="growth",
            field=models.DecimalField(
                decimal_places=3,
                max_digits=5,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="may",
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="may_normalized",
            field=models.DecimalField(
                decimal_places=3,
                max_digits=5,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="popularity",
            field=models.DecimalField(
                decimal_places=3,
                max_digits=5,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="tts",
            field=models.DecimalField(
                decimal_places=3,
                max_digits=5,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
    ]