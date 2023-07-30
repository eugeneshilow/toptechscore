# Generated by Django 4.2.2 on 2023-07-05 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ai_tools", "0010_remove_photo_ai_tool_alter_photo_image_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhotoURL",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name="photo",
            name="image_url",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ai_tools.photourl"
            ),
        ),
    ]