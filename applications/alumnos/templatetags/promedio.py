from django import template
register = template.Library()

@register.simple_tag
def prom_especifico(lista):
    lista = list(lista)
    if len(lista) > 0:
        total = len(lista)
        result = 0
        for n in lista:
            result+= n.calificacion
        return round(float(result/total),1)
        # return "{:.1f}".format(float(result/total))
    else:
        return ''

@register.simple_tag
def get_notas(asignatura, alumno):
    notas=[]
    for nota in asignatura.parciales.all():
        if nota.alumno.rut == alumno.rut:
            notas.append(nota)
    return notas
   



@register.simple_tag
def prom_global(asignaturas, alumno):
    asignaturas = list(asignaturas)
    especificos = []
    for asign in asignaturas:
        if len(asign.parciales.all()) !=0:
            notas=[]
            for n in asign.parciales.all():
                if n.alumno.rut == alumno.rut:
                    notas.append(n.calificacion)
            if len(notas) !=0:
                especificos.append(sum(notas)/len(notas))
    if len(especificos) !=0:
        return round(float(sum(especificos)/len(especificos)),1)
    else:
        return ''
    # return "{:.1f}".format(float(sum(especificos)/len(especificos)))

    