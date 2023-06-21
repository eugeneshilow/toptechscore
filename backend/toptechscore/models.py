from django.db import models

class AITool(models.Model):
    name = models.CharField(max_length=200)
    monthly_traffic = models.IntegerField()
    time_spent_on_website = models.DurationField()
    # add any other fields that you need
