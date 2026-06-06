from django import template

register = template.Library()

@register.simple_tag
def update_variable(b, c):
    a = None
    if b:
        a=b
    elif c:
        a=c
    return a

