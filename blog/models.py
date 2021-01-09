from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    thumbnail = models.ImageField(upload_to='thumbnails')
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    uploaded_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
