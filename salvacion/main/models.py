from django.db import models

from .utils import from_cyrillic_to_eng


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.title))
        super().save(*args, **kwargs)

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()  # Убедитесь, что это поле определено в вашей модели
    message = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=True)

