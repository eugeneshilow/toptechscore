# Generated by Django 4.2.2 on 2023-07-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ai_tools", "0015_remove_aitool_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="aitool",
            name="logo",
            field=models.URLField(blank=True, null=True),
        ),
    ]
