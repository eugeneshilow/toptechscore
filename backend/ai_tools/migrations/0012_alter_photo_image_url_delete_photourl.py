# Generated by Django 4.2.2 on 2023-07-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ai_tools", "0011_photourl_alter_photo_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo", name="image_url", field=models.URLField(),
        ),
        migrations.DeleteModel(name="PhotoURL",),
    ]
