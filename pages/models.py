from django.db import models
from ckeditor.fields import RichTextField
from .validadores import validarMayusculas,validarNE,validarIdentificacion

class Page(models.Model):
    COLOMBIA = 'CO'
    ESTADOSUNIDOS = 'US'
    PAISE_CHOICES = [
        (COLOMBIA, 'Colombia'),
        (ESTADOSUNIDOS, 'Estados Unidos'),
    ]
    CEDULA = 'CC'
    EXTRANJERIA = 'CEXT'
    PASAPORTE = 'PASSP'
    PERMISO = 'PER_ESP'
    TIPO_ID_CHOICES = [
        (CEDULA, 'Cédula de Ciudadanía'),
        (EXTRANJERIA, 'Cédula de Extranjería'),
        (PASAPORTE, 'Pasaporte'),
        (PERMISO, 'Permiso Especial'),
    ]
    nombre1 = models.CharField(verbose_name="Primer Nombre", max_length=20,validators=[validarMayusculas,validarNE])
    nombre2 = models.CharField(verbose_name="Primer Nombre", max_length=50,validators=[validarMayusculas,validarNE])
    apellido1 = models.CharField(verbose_name="Primer Apellido", max_length=20,validators=[validarMayusculas,validarNE])
    apellido2 = models.CharField(verbose_name="Segundo Apellido", max_length=20,validators=[validarMayusculas,validarNE])
    pais = models.CharField(
        max_length=2,
        choices=PAISE_CHOICES,
        default=COLOMBIA,
    )
    tipoId = models.CharField(
        max_length=7,
        choices=TIPO_ID_CHOICES,
        default=CEDULA,
    )
    numeroId = models.CharField(verbose_name="-	Número de Identificación", max_length=20,validators=[validarIdentificacion])
    fechaIngreso = models.DateField(auto_now_add=False, verbose_name="Fecha de Ingreso")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'nombre1']

    def __str__(self):
        return self.nombre1 + self.nombre2 + self.apellido1 + self.apellido2
