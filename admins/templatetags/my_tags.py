from django.conf import settings
from django import template

register = template.Library()


def media_folder_product(string):
    if not string:
        string = 'products_images/default.jpg'
    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='media_folder_products')
def media_folder_users(string):
    if not string:
        string = 'avatars/default.jpg'

    return f'{settings.MEDIA_URL}{string}'


register.filter('media_folder_products', media_folder_product)