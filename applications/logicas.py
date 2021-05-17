import sys
from itertools import cycle
def validar_rut(rut):
    rut = rut.upper()
    rut = rut.replace("-","")
    rut = rut.replace(".","")
    aux = rut[:-1]
    dv = rut[-1:]   
    
    if rut.isdigit():
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
    else:
        return False