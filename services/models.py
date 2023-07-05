from django.db import models

# Create your models here.

class Services(models.Model):
    tile1 = models.CharField(max_length=264)
    title2 = models.CharField(max_length=264)
    image = models.ImageField()
    description = models.TextField(max_length=600)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "services"
        verbose_name_plural = "Services"
        ordering = ["-created"]

    def __str__(self):
        return self.tile1
