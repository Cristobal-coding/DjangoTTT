from django.forms import ValidationError
from itertools import cycle

def validar_rut_formulario(value):
    value = value.upper()
    value = value.replace("-","")
    value = value.replace(".","")
    aux = value[:-1]
    dv = value[-1:] 
    rutAux = value[0: len(value)-1]  

    if rutAux.isdigit():
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11
        if str(res) != dv:
            raise ValidationError("RUT Inválido")
        elif dv!="K" and res!=10:
            raise ValidationError("RUT Inválido")
           
    else:
        raise ValidationError("El RUT debe ser numerico")
    return value

def validar_rut(value):
    value = value.upper()
    value = value.replace("-","")
    value = value.replace(".","")
    aux = value[:-1]
    dv = value[-1:] 
    rutAux = value[0: len(value)-1]  

    if rutAux.isdigit():
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11
        if str(res) == dv:
            return True
        elif dv=="K" and res==10:
            return True
           
    else:
        return False
    return False