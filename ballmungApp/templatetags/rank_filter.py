from django import template

register = template.Library()

@register.filter
def rank_filter(value, arg):
    rank = value + (arg - 1) * 10
    return rank