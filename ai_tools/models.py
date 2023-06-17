from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class AITool(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, null=True)
    sub_category = models.CharField(max_length=255, null=True)
    website = models.URLField(max_length=200, null=True)
    description = models.TextField(null=True)
    february = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    april = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    may = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    average_time_on_website = models.DecimalField(max_digits=12, decimal_places=2, null=True) 
    may_normalized = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    change_normalized = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    average_time_normalized = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    tts = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    popularity = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    growth = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    engagement = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])

    class Meta:
        indexes = [
            models.Index(fields=['name',], name='name_idx'),
        ]

    def __str__(self):
        return self.name
