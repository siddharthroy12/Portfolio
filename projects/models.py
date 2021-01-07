from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=30)
    tech_stack = models.CharField(max_length=50)
    desc = models.TextField()
    featured = models.BooleanField(default=False)
    preview = models.ImageField(upload_to='previews')
    live_link = models.CharField(max_length=500, blank=True)
    github_link = models.CharField(max_length=400, blank=True)

    def __str__(self):
        return self.name