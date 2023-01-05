from django import template

register = template.Library()

@register.filter
def time_filter(value):
    text = "{f}.{b}초"
    return text.format(f=(value//100), b=(value%100))