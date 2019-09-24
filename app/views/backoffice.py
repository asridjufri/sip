from django.shortcuts import render
from app.models import Appmenu, MasterJenis, Appgroup

def test(request):
    return render(request,'app/index.html')

def menu(request):
    menus = Appmenu.objects.filter(deleted=0, module__modulename__isnull=False)
    return render(request, 'app/menu.html',{'menus':menus})

def data_jenis(request):
    data_jenis_list = MasterJenis.objects.filter(deleted=0)
    return render(request, 'app/data-jenis.html', {'data_jenis_list':data_jenis_list})

def groups(request):
    group_list = Appgroup.objects.filter(deleted=0)
    return render(request, 'app/cms-group.html',{'group_list':group_list})


