from django import template
from app.models import MasterCategory, MasterJenis, Appgroup, Appuser, Appmenu
from app.services import MenuService
register=template.Library()

@register.inclusion_tag('app/tags/menu.html')
def load_menu(user):
    allowed_menus = MenuService.get_allowed_menus('admin')
    return {'allowed_menus':allowed_menus}
    
    
@register.inclusion_tag('app/tags/charts/tourism-pendapatan.html')
def chart_tourism_vs_pendapatan(container_id):
    return {'container_id':container_id}

@register.inclusion_tag('app/tags/charts/tourism-pendapatan-annual.html')
def chart_tourism_vs_pendapatan_annual(container_id):
    return {'container_id':container_id}

@register.inclusion_tag('app/tags/charts/tourism-pendapatan-monthly.html')
def chart_tourism_vs_pendapatan_monthly(container_id):
    return {'container_id':container_id}

@register.inclusion_tag('app/tags/charts/tourism-negara-annual.html')
def chart_tourism_vs_negara(container_id):
    return {'container_id':container_id}