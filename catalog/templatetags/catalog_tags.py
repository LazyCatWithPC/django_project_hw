from django import template
from config import settings

register = template.Library()


@register.simple_tag()
def media_path(image_name):
    return f'{settings.MEDIA_URL}{image_name}'


@register.filter()
def media_path(image_name):
    return f'{settings.MEDIA_URL}{image_name}'
