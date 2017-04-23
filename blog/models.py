from django.db import models

# Create your models here.

from django.conf import settings
from django.utils.functional import total_ordering


class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)
    titulo = models.CharField(max_length=100, unique=True)
    fecha = models.DateField()
    contenido = models.TextField()
    slug = models.SlugField()

    class Meta:
        ordering = ['autor']
        verbose_name_plural = "Posts"

    def __unicode__(self):
        return '%s - %s' %(self.autor, self.titulo)
