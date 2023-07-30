from django import forms
from django.contrib import admin
from .models import AITool, Photo, PhotoBatch

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['image_url'] 

class PhotoBatchForm(forms.ModelForm):
    class Meta:
        model = PhotoBatch
        fields = ['urls']

    def save(self, commit=True):
        instance = super().save(commit=False)
        urls = [url.strip() for url in self.cleaned_data['urls'].split(',')]
        photos = [Photo(image_url=url) for url in urls]
        Photo.objects.bulk_create(photos)
        return instance

class PhotoBatchAdmin(admin.ModelAdmin):
    form = PhotoBatchForm

class AIToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'sub_category', 'website', 
                    'february', 'april', 'may', 'average_time_on_website', 
                    'may_normalized', 'change_normalized', 'average_time_normalized', 
                    'tts', 'popularity', 'growth', 'engagement']
    search_fields = ['name', 'category', 'sub_category']  # Include the fields you want to search by
    list_filter = ['category', 'sub_category']  # Include the fields you want to filter by
    filter_horizontal = ['explanation_photos']

admin.site.register(AITool, AIToolAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoBatch, PhotoBatchAdmin)  
