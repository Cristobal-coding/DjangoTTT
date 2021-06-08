from django import template
register = template.Library()

@register.simple_tag
def id_compare(rol_id,message):
    rol_id = str(rol_id).strip()
    message = str(message).strip()
    print('Los parametros: ',rol_id,message)
    unique =False
    title=False

    if rol_id in message:
        unique=True
        if '*' in message:
            title=True      
            
    return{
        'unique': unique,
        'title': title,
    }
