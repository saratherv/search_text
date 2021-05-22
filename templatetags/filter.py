import datetime
from django import template
    
register = template.Library()

@register.filter(name="get_url")
def get_url(input):
    return input["_source"]["url"]


@register.filter(name="get_name")
def get_name(input):
    return input["_source"]["file_name"]


register.filter('get_name', get_name)
register.filter('get_url', get_url)