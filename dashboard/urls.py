from django.urls import path
from django.conf.urls import url
from dashboard.views import slide1, dashboard1, sample, dashboard2, get_chart_number_tourism_per_category_per_year
from dashboard import views
urlpatterns = [
    url(r'^slider1$', slide1),
    url(r'^dashboard$', views.dashboard_dynamic, name='dynamic-dashboard'),
    url(r'^sample$', sample),
    url(r'^dashboard1$', dashboard1),
    url(r'^dashboard2$', dashboard2),
    url(r'^dashboard3$', views.dashboard3),
    url(r'^data/number-tourism-per-category-per-year$', get_chart_number_tourism_per_category_per_year, name='number-tourism-per-category-per-year'),
    url(r'^data/number-tourism-per-category-per-month$', views.get_chart_number_tourism_per_category_per_month, name='number-tourism-per-category-per-month'),
    url(r'^data/number-tourism-per-category-per-year-domestic-mancanegara$', views.get_chart_number_tourism_per_category_per_year_domestic_mancanegara, name='number-tourism-per-category-per-year-domestic-mancanegara'),
    url(r'^data/number-domestic-mancanegara-at-year$', views.get_number_domestic_mancanegara_at_year, name='number-domestic-mancanegara-at-year'),
    url(r'^data/number-tourist-per-categories-at-year$', views.get_number_tourist_per_categories_at_year , name='number-tourist-per-categories-at-year'),
    url(r'^data/get-number-tourism-per-category-per-month-domestic-mancanegara$', views.get_number_tourism_per_category_per_month_domestic_mancanegara , name='get-number-tourism-per-category-per-month-domestic-mancanegara'),
    url(r'^data/get-number-tourism-per-categories-per-month-domestic$', views.get_number_tourism_per_categories_per_month_domestic , name='get-number-tourism-per-categories-per-month-domestic'),
    url(r'^data/get-number-tourism-per-categories-per-month-mancanegara$', views.get_number_tourism_per_categories_per_month_mancanegara , name='get-number-tourism-per-categories-per-month-mancanegara'),
    
   
]
