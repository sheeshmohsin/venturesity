from django import template
register = template.Library()

@register.filter(name='cons')
def cons(pk):
    return pk.encode('utf8')

@register.filter(name='private')
def private(obj):
    return obj['_id']
