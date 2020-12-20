from django import template
from django.utils.safestring import mark_safe

from wagtail.core.rich_text import RichText, expand_db_html

register = template.Library()

@register.filter
def richtext_withclasses(value):
    if isinstance(value, RichText):
        html = expand_db_html(value.source)
    elif isinstance(value, str):
        html = expand_db_html(value)
    elif value is None:
        html = ""
    else:
        raise TypeError(
            "'richtext_withclasses' template filter received an invalid value; expected string, got {}.".format(
                type(value)
            )
        )

    return mark_safe(html)