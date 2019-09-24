from django.shortcuts import render
from django.http import JsonResponse
from dashboard.services import ChartService
from datetime import datetime
from django.urls import reverse_lazy
from dashboard.models import Dashboard, Slide
# Create your views here.
def slide1(request):
    return render(request,'dashboard/reveal/index.html')
def dashboard_dynamic(request):
    id = request.GET.get('id',1)
    dashboard = Dashboard.objects.get(pk=id)
    print(dashboard)
    slides = Slide.objects.filter(dashboard=dashboard).order_by('order')
    print(slides)
    return render(request,'dashboard/reveal/dashboard.html',{'dashboard':dashboard, 'slides':slides})

def sample(request):
    return render(request, 'dashboard/index.html')
def dashboard1(request):
    return render(request, 'dashboard/dashboard1.html')
def dashboard2(request):
    return render(request, 'dashboard/dashboard2.html')
def dashboard3(request):
    year=request.GET.get('year',datetime.now().year)
    kecamatan=request.GET.get('kecamatan',None)
    return render(request, 'dashboard/dashboard3.html',{'year':year,'kecamatan':kecamatan})

def get_chart_number_tourism_per_category_per_year(request):
    categoryid=request.GET.get('category','MICE')
    print(categoryid)
    data = ChartService.get_chart_number_tourism_per_category_per_year(categoryid)
    
    return JsonResponse(data)

def get_chart_number_tourism_per_category_per_month(request):
    categoryid=request.GET.get('category','MICE')
    now = datetime.now()
    default_year = now.year
    year = request.GET.get('year',default_year)
    data = ChartService.get_chart_number_tourism_per_category_per_month(categoryid,year)
    
    return JsonResponse(data)

def get_chart_number_tourism_per_category_per_year_domestic_mancanegara(request):
    categoryid=request.GET.get('category','MICE')
    
    data = ChartService.get_chart_number_tourism_per_category_per_year_domestic_mancanegara(categoryid)
    
    return JsonResponse(data)

def get_number_domestic_mancanegara_at_year(request):
    tahun = request.GET.get('year',datetime.now().year)
    name_kecamatan=request.GET.get('kecamatan')
    kecamatan=ChartService.get_kecamatan_by_name(name_kecamatan)
    idkecamatan = None
    if kecamatan:
        idkecamatan = kecamatan.kecamatanid
    data = ChartService.get_number_domestic_mancanegara_at_year(tahun,idkecamatan)
    return JsonResponse(data)

def get_number_tourist_per_categories_at_year(request):
    tahun = request.GET.get('year',datetime.now().year)
    name_kecamatan=request.GET.get('kecamatan')
    kecamatan=ChartService.get_kecamatan_by_name(name_kecamatan)
    idkecamatan = None
    if kecamatan:
        idkecamatan = kecamatan.kecamatanid
    data = ChartService.get_number_tourist_per_categories_at_year(tahun, idkecamatan)
    return JsonResponse(data)

def get_number_tourism_per_category_per_month_domestic_mancanegara(request):
    tahun = request.GET.get('year',datetime.now().year)
    name_kecamatan=request.GET.get('kecamatan')
    kecamatan=ChartService.get_kecamatan_by_name(name_kecamatan)
    idkecamatan = None
    if kecamatan:
        idkecamatan = kecamatan.kecamatanid
    data = ChartService.get_number_tourism_per_category_per_month_domestic_mancanegara(tahun, idkecamatan)
    return JsonResponse(data)

def get_number_tourism_per_categories_per_month_domestic(request):
    tahun = request.GET.get('year',datetime.now().year)
    name_kecamatan=request.GET.get('kecamatan')
    kecamatan=ChartService.get_kecamatan_by_name(name_kecamatan)
    idkecamatan = None
    if kecamatan:
        idkecamatan = kecamatan.kecamatanid
    data = ChartService.get_number_tourism_per_categories_per_month_domestic(tahun, idkecamatan)
    return JsonResponse(data)

def get_number_tourism_per_categories_per_month_mancanegara(request):
    tahun = request.GET.get('year',datetime.now().year)
    name_kecamatan=request.GET.get('kecamatan',None)
    kecamatan=ChartService.get_kecamatan_by_name(name_kecamatan)
    idkecamatan = None
    if kecamatan:
        idkecamatan = kecamatan.kecamatanid
    data = ChartService.get_number_tourism_per_categories_per_month_mancanegara(tahun, idkecamatan)
    return JsonResponse(data)
