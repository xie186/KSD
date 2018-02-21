from django.db import models

# Create your models here.
class DownloadFile(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    description = models.CharField(max_length=256)
    slug = models.SlugField()

    def __str__(self):
        return self.name

