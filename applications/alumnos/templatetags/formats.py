from django import template
from datetime import date, datetime
import math
register = template.Library()

@register.simple_tag
def date_to_age(nacimiento):
    age=''
    if nacimiento:
        current = date.today()
        result = current - nacimiento
        result= str(result)
        result = result.split(" ",1)
        days = result[0]
        days = int(days)
        age= days / 365
        age=math.floor(age)
    return age
    
@register.simple_tag
def sin_especificar(total, m , f):
    sin = int(total)-(int(m)+int(f))
    return sin

@register.simple_tag
def path_with_filter(path):
    if 'csrf' in path:
        path ='&'+path[path.index('csrf'):len(path)]
    else:
        path=''
    return path

# ?csrfmiddlewaretoken=rmStQ97R8EHreQY3yIjPbi7RTdxfTSVDW4zZ1ubFYlih75IwuyisXdhdNeQnCMZp&kword=F&fecha1=2006-05-12&fecha2=2021-05-11&sexo=1
@register.simple_tag
def keep_filters(path):
    key=''
    minimo=''
    maximo=''
    gender=''
    if 'csrf' in path:
        key=path[path.index('kword')+6:path.index('fecha1')-1]
        minimo=path[path.index('fecha1')+7:path.index('fecha2')-1]
        maximo=path[path.index('fecha2')+7:path.index('sexo')-1]
        gender=path[len(path)-1:len(path)]
    return {
        'key': key,
        'minimo': minimo,
        'maximo': maximo,
        'gender': gender,
    }
#?csrfmiddlewaretoken=vrsLtK0JYQLobkcj0tAkrbD9kSYrex6p1ROGBJW6a9omyMAGoWTjYNywcIakXgQQ&nombre=a&rut=2    
@register.simple_tag
def keep_filters_apod(path):
    rut=''
    nombre=''
    if 'csrf' in path:
        nombre=path[path.index('nombre')+7:path.index('rut')-1]
        rut=path[path.index('rut')+4:len(path)]
    return {
        'nombre': nombre,
        'rut': rut

    }
