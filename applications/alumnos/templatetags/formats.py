from django import template
from datetime import date, datetime
from datetime import timedelta

register = template.Library()

@register.simple_tag
def date_to_age(nacimiento):
    current = date.today()
    result = current - nacimiento
    result= str(result)
    result = result.split(" ",1)
    days = result[0]
    days = int(days)
    print(type(days))
    # age= days / 365
    return days
