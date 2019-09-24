from django import template
from app.models import MasterCategory, MasterJenis, Appgroup, Appuser, Appmenu
from app.services import MenuService
from django.urls import reverse_lazy
register=template.Library()

@register.inclusion_tag('dashboard/tags/menu.html')
def load_menu(user):
    allowed_menus = MenuService.get_allowed_menus('admin')
    return {'allowed_menus':allowed_menus}
    
    
@register.inclusion_tag('dashboard/tags/charts/tourism-pendapatan.html')
def chart_tourism_vs_pendapatan(container_id):
    return {'container_id':container_id}

@register.inclusion_tag('dashboard/tags/charts/tourism-pendapatan-annual.html')
def chart_tourism_vs_pendapatan_annual(container_id):
    return {'container_id':container_id}

@register.inclusion_tag('dashboard/tags/charts/tourism-pendapatan-monthly.html')
def chart_tourism_vs_pendapatan_monthly(container_id):
    return {'container_id':container_id}

@register.inclusion_tag('dashboard/tags/charts/number-tourism-per-category-per-year.html')
def chart_number_tourism_per_category_per_year(container_id,chart_type,category_id):
    url = reverse_lazy('number-tourism-per-category-per-year')
    url = "%s?category=%s"%(url, category_id)
    return {'url':url, 'container_id':container_id,'category_id':category_id, 'chart_type':chart_type}

@register.inclusion_tag('dashboard/tags/charts/number-tourism-per-category-per-month.html')
def chart_number_tourism_per_category_per_month(container_id,chart_type, category_id,year):
    url=reverse_lazy('number-tourism-per-category-per-month')
    url="%s?categoryid=%s&year=%s" %(url, category_id, year)
    return {'container_id':container_id,'category_id':category_id,'year':year,'chart_type':chart_type, 'url':url}

@register.inclusion_tag('dashboard/tags/charts/number-tourism-per-category-per-year.html')
def chart_number_tourism_per_category_per_year_domestic_mancanegara(container_id,chart_type,category_id):
    url = reverse_lazy('number-tourism-per-category-per-year-domestic-mancanegara')
    url = "%s?category=%s"%(url, category_id)
    return {'url':url, 'container_id':container_id,'category_id':category_id, 'chart_type':chart_type}

@register.inclusion_tag('dashboard/tags/charts/pie.html')
def get_number_domestic_mancanegara_at_year(container_id, ayear, kecamatan=None):
    url = reverse_lazy('number-domestic-mancanegara-at-year')
    
    url = "%s?year=%s&kecamatan=%s"%(url,ayear,kecamatan)
    return {'url':url, 'container_id':container_id}


@register.inclusion_tag('dashboard/tags/charts/pie.html')
def get_number_tourist_per_categories_at_year(container_id, ayear, kecamatan=None):
    
    url = reverse_lazy('number-tourist-per-categories-at-year')
    url = "%s?year=%s&kecamatan=%s"%(url,ayear, kecamatan)
    return {'url':url, 'container_id':container_id}

@register.inclusion_tag('dashboard/tags/charts/number-tourism-per-category-per-month.html')
def get_number_tourism_per_category_per_month_domestic_mancanegara(container_id,chart_type, ayear, kecamatan=None):
    url = reverse_lazy('get-number-tourism-per-category-per-month-domestic-mancanegara')
    url = "%s?year=%s&kecamatan=%s"%(url,ayear,kecamatan)
    return {'url':url, 'container_id':container_id,'chart_type':chart_type}

@register.inclusion_tag('dashboard/tags/charts/number-tourism-per-category-per-month.html')
def get_number_tourism_per_categories_per_month_domestic(container_id, chart_type, ayear,kecamatan):
    url = reverse_lazy('get-number-tourism-per-categories-per-month-domestic')
    url = "%s?year=%s&kecamatan=%s"%(url,ayear,kecamatan)
    return {'url':url, 'container_id':container_id,'chart_type':chart_type}

@register.inclusion_tag('dashboard/tags/charts/number-tourism-per-category-per-month.html')
def get_number_tourism_per_categories_per_month_mancanegara(container_id, chart_type, ayear, kecamatan):
    url = reverse_lazy('get-number-tourism-per-categories-per-month-mancanegara')
    url = "%s?year=%s&kecamatan=%s"%(url,ayear,kecamatan)
    return {'url':url, 'container_id':container_id,'chart_type':chart_type}


