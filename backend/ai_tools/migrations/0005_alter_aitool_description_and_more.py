# Generated by Django 4.2.2 on 2023-07-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ai_tools", "0004_aitool_explanation_video_aitool_logo_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aitool",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="long_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="medium_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="review_text",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="short_description",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="aitool",
            name="vote_count",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]