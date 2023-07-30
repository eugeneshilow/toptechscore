# Generated by Django 4.2.2 on 2023-07-05 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ai_tools", "0008_rename_feedback_aitool_pricing"),
    ]

    operations = [
        migrations.RemoveField(model_name="photo", name="image",),
        migrations.AddField(
            model_name="photo",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]