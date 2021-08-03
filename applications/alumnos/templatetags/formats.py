import math
from datetime import date
from django import template
register = template.Library()

@register.simple_tag
def days_periodo(inicio, termino):
    current = date.today()
    if termino is None:
        return 'En curso'
    else:
        result = inicio - termino
        result= str(result)
        result = result.split(" ",1)
        days = result[0]        
        return math.floor(int(days))

@register.simple_tag
def date_to_age(nacimiento):
    age=''
    if nacimiento:
        current = date.today()
        result = current - nacimiento
        result= str(result)
        result = result.split(" ",1)
        days = result[0]
        if days != '0:00:00':
            days = int(days)
            age= days / 365
            age=math.floor(age)
        else:
            age='0'
    return age
    
@register.simple_tag
def sin_especificar(total, m , f):
    sin = int(total)-(int(m)+int(f))
    return sin

@register.simple_tag
def path_with_filter(path):
    print('PATH: ', path)
    if '?' in path and not 'page' in path:
        path = '&'+path[path.index('?')+1:len(path)]
    elif 'page' in path and 'kword' in path and 'fecha1' in path and 'fecha2' in path and 'sexo' in path :
        path =path[path.index('&'):len(path)]
    else:
        path=''
    return path

@register.simple_tag
def path_with_filter_cursos(path):
    if '?' in path and not 'page' in path:
        path = '&'+path[path.index('?')+1:len(path)]
    elif 'page' in path and 'id' in path and 'year' in path and 'semestre' in path and 'jefe' in path :
        path =path[path.index('&'):len(path)]
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
    curso=''
    if 'kword' in path and 'fecha1' in path and 'fecha2' in path and 'curso' in path and 'sexo' in path :
        key=path[path.index('kword')+6:path.index('fecha1')-1]
        minimo=path[path.index('fecha1')+7:path.index('fecha2')-1]
        maximo=path[path.index('fecha2')+7:path.index('curso')-1]
        curso=path[path.index('curso')+6:path.index('sexo')-1]
        gender=path[len(path)-1:len(path)]
    return {
        'key': key,
        'minimo': minimo,
        'maximo': maximo,
        'gender': gender,
        'curso': curso,
    }
#?csrfmiddlewaretoken=vrsLtK0JYQLobkcj0tAkrbD9kSYrex6p1ROGBJW6a9omyMAGoWTjYNywcIakXgQQ&nombre=a&rut=2    
@register.simple_tag
def keep_filters_apod(path):
    rut=''
    nombre=''
    if 'nombre' in path and 'rut' in path:
        nombre=path[path.index('nombre')+7:path.index('rut')-1]
        rut=path[path.index('rut')+4:len(path)]
    return {
        'nombre': nombre,
        'rut': rut

    }

@register.simple_tag
def keep_filters_cursos(path):
    id=''
    jefe=''
    year=''
    semestre=''
    if 'id' in path and 'jefe' in path and 'year' in path and 'semestre' in path :
        id=path[path.index('id')+3:path.index('year')-1]
        year=path[path.index('year')+5:path.index('semestre')-1]
        semestre=path[path.index('semestre')+9:path.index('jefe')-1]
        jefe=path[path.index('jefe')+5:len(path)]
    if year != '':
        year = int(year)

    if jefe != '' and jefe != '=' and id == '':
        # jefe = int(jefe)
        year = ''
        semestre = ''

    if id != '':
        jefe = ''
    return {
        'id': id,
        'jefe': jefe,
        'year': year,
        'semestre': semestre,
    }
