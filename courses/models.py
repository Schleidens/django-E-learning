from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.utils.text import slugify

# Create your models here.


class coursesModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=(
        "Author"), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False)
    cover = models.ImageField(upload_to='courses')
    description = RichTextField()
    duration = models.PositiveIntegerField()
    intro_video = models.URLField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
