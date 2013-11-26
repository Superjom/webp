from django import template

register = template.Library()

@register.simple_tag
def include_script(path):
    return "<script src='/static/%s'></script>" % path

@register.simple_tag
def include_style(path):
    return "<link rel='stylesheet' href='/static/%s' type='text/css'/>" % path

@register.simple_tag
def _import(path):
    if path.endswith('.js'):
        return "<script src='/static/%s'></script>" % path
    elif path.endswith('.css'):
        return "<link rel='stylesheet' href='/static/%s' type='text/css'/>" % path

@register.filter(name='is_in')
def is_in(value, arg):
    return value in arg
