from django.template import Library

from fnotes.models import EntryTag

register = Library()


@register.inclusion_tag('fnotes/menu_tags.html')
def notes_tags(*args):
    tags = EntryTag.objects.all()
    return {'tag_list': tags}