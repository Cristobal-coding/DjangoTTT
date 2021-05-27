from django import template
from datetime import date
import math
register = template.Library()

@register.simple_tag
def date_to_age(nacimiento):
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
