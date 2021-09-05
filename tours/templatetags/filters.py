from typing import Union

from django import template

from tours import data

register = template.Library()


@register.filter
def stars(number: Union[int, str]):
    return '★' * int(number)


@register.filter
def from_city(format_string):
    return data.departures[format_string][0].lower() + data.departures[format_string][1:]


@register.filter
def ru_pluralize(number: Union[int, str], arg: str = 'дурак,дурака,дураков'):
    nominative_singular, genitive_singular, genitive_plural = arg.split(',')
    number = abs(int(number))

    if 10 <= number % 100 <= 20:
        return f'{number} {genitive_plural}'
    if number % 10 == 1:
        return f'{number} {nominative_singular}'
    if 2 <= number % 10 <= 4:
        return f'{number} {genitive_singular}'
    return f'{number} {genitive_plural}'
