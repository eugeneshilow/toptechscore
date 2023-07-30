# Generated by Django 4.2.2 on 2023-07-01 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ai_tools", "0003_aitool_description_perplexity"),
    ]

    operations = [
        migrations.AddField(
            model_name="aitool",
            name="explanation_video",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="aitool",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="logos/"),
        ),
        migrations.AddField(
            model_name="aitool",
            name="long_description",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="aitool",
            name="medium_description",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="aitool", name="review_text", field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="aitool",
            name="review_video",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="aitool",
            name="short_description",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="aitool",
            name="vote_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name="Photo",
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
                ("image", models.ImageField(upload_to="photos/")),
                (
                    "ai_tool",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="ai_tools.aitool",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="aitool",
            name="explanation_photos",
            field=models.ManyToManyField(blank=True, to="ai_tools.photo"),
        ),
    ]