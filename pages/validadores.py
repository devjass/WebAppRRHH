from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as gl

def validarMayusculas(value):   #Válida si todas son mayúsculas
    if(str(value).isupper()):
        pass
    else:
        raise ValidationError(
            gl('Nombre:%(value)s Tiene que ser todas Mayúsculas'),
            params={'value': value},
        )

def validarNE(value):           #Válida si tiene Ñ
    if("Ñ" in value):
        raise ValidationError(
            gl('Nombre:%(value)s No puede tener Ñ'),
            params={'value': value},
        )

def validarIdentificacion(value):#Válida si es alfanúmerico
    if(not str(value).isalnum()):
        raise ValidationError(
            gl('Cédula:%(value)s  debe ser alfanúmerica'),
            params={'value': value},
        )