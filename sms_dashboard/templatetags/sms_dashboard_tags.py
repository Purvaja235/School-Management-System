from django import template

register = template.Library()

@register.filter
def replace_underscore(value):
    """Converts a string into all uppercase"""
    return value.replace('_',' ')
