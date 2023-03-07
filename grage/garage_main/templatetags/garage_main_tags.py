from django import template
from garage_main.models import *

register = template.Library()


@register.simple_tag(name='Models_Auto')
def ModelAdd_models():
    return ModelAdd.objects.all()


@register.inclusion_tag('garage_main/link_base.html')
def AutoModels_link(cat_select):
    if cat_select:
        posts = AutoModels.objects.filter(model_add=cat_select).select_related('group_add')
    else:
        posts = AutoModels.objects.all().select_related('group_add')
    return {'posts': posts}

