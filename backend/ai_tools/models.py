from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from urllib.parse import urlparse
import os

class Photo(models.Model):
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.image_url
    
class PhotoBatch(models.Model):
    urls = models.TextField(help_text="Enter URLs separated by comma ','")

class AITool(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    website = models.URLField(max_length=200, null=True)
    favicon_url = models.URLField(max_length=200, null=True, blank=True)
    february = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    april = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    may = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    average_time_on_website = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    may_normalized = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    change_normalized = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    average_time_normalized = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(1)])

    type = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    sub_category = models.CharField(max_length=255, null=True)
    
    tts = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    tts_rank = models.PositiveIntegerField(default=0, editable=False)
    
    popularity = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    growth = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    engagement = models.DecimalField(max_digits=5, decimal_places=3, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    
    description = models.TextField(null=True, blank=True)
    description_perplexity = models.TextField(null=True, blank=True)
    short_description = models.CharField(max_length=255, null=True, blank=True)
    logo = models.URLField(max_length=200, null=True, blank=True)
    vote_count = models.PositiveIntegerField(default=0, blank=True)
    explanation_video = models.URLField(max_length=200, null=True, blank=True)
    review_text = models.TextField(null=True, blank=True)

    pros = models.TextField(null=True, blank=True)
    cons = models.TextField(null=True, blank=True)
    explanation_photos = models.ManyToManyField(Photo, blank=True)
    review_video = models.URLField(max_length=200, null=True, blank=True)
    brief_description = models.TextField(null=True, blank=True)
    key_features = models.TextField(null=True, blank=True)
    pricing = models.TextField(null=True, blank=True)
    comparison = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # only for new objects
            max_rank = AITool.objects.all().aggregate(largest=models.Max('tts_rank'))['largest']

            if max_rank:
                self.tts_rank = max_rank + 1
            else:
                self.tts_rank = 1

        super(AITool, self).save(*args, **kwargs)    
    
    @property
    def full_favicon_url(self):
        if self.favicon_url is None:
            return None

        parsed = urlparse(self.favicon_url)
        if bool(parsed.netloc):
            return self.favicon_url
        else:
            return os.path.join(os.getenv('CLOUDINARY_URL'), self.favicon_url)

    class Meta:
        db_table = 'aitool'  # Set the table name
        ordering = ['-tts']  # Order by tts in descending order
        indexes = [
            models.Index(fields=['name',], name='name_idx'),
        ]

    def __str__(self):
        return self.name

class SearchQuery(models.Model):
    STATUS_PENDING = 0
    STATUS_RUNNING = 1
    STATUS_COMPLETED = 2
    STATUS_ERROR = 3

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_RUNNING, 'Running'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_ERROR, 'Error'),
    ]

    ai_tool = models.ForeignKey(AITool, on_delete=models.CASCADE, related_name='search_queries')
    query = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_PENDING)
    result = models.TextField(null=True, blank=True)
    error_message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.query
