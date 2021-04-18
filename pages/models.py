from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    nombre1 = models.CharField(verbose_name="Primer Nombre", max_length=200)
    nombre2 = models.CharField(verbose_name="Segundo Nombre")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'nombre1']

    def __str__(self):
        return self.nombre1 + self.nombre2
