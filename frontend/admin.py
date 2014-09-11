from frontend.models import Video
from django.contrib import admin

# Presentation
class VideoAdmin(admin.ModelAdmin):
    fields = [
        'filename', 
        'title',
        'category', 
        'description'
    ]

admin.site.register(Video, VideoAdmin)
