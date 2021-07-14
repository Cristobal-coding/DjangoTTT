from django import template
import random
register = template.Library()

@register.simple_tag
def random_number():
    num = random.randrange(10)  
    num+=1
    return str(num)
