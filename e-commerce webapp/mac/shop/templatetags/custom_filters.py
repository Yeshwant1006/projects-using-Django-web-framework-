from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Gets an item from a dictionary using the key."""
    try:
        return dictionary[key]
    except KeyError:
        return None

@register.filter
def multiply(value, arg):
    """Multiplies the value by the arg."""
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0


