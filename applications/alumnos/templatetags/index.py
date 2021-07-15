from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    indexable = list(indexable)
    if len(indexable) == 0:
        return ''
    elif len(indexable)-1 >= i :
        return indexable[i].calificacion
    else:
        return ''

@register.filter
def fecha(indexable, i):
    indexable = list(indexable)
    if len(indexable) == 0:
        return ''
    elif len(indexable)-1 >= i :
        return indexable[i].fecha
    else:
        return ''