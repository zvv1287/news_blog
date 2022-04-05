from django import template

from pages.models import Pages

register = template.Library()


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def page_list(context):
    """template tag вывода категорий"""
    pages = Pages.objects.all()
    template = 'base/blog/pages.html'
    return {'template': template, "pages_list": pages}
