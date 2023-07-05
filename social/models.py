from django.db import models


# Create your models here.

class Link(models.Model):
    key = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "social"
        verbose_name_plural = "sociales"
        ordering = ["name"]

    def __str__(self):
        return self.name
