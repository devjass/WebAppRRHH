from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as gl

def validarMayusculas(value):
    if(str(value).isupper()):
        pass
    else:
        raise ValidationError(
            gl('Nombre:%(value)s Tiene que ser todas Mayúsculas'),
            params={'value': value},
        )

def validarNE(value):
    if("Ñ" in value):
        raise ValidationError(
            gl('Nombre:%(value)s No puede tener Ñ'),
            params={'value': value},
        )