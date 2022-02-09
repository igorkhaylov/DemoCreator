from django import template
from main.models import News

register = template.Library()


@register.simple_tag()
def get_last_posts():
    return News.objects.filter(is_published=True)[:3]

