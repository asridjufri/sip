from django.shortcuts import render
from app.services import ModuleService

# def _get_
def home(request, appmenu):
    return render(request, 'app/sliders/index.html')
def menu(request, appmenu):
    menus = ModuleService.menu_list()
    return render(request, 'app/menu.html',{'menus':menus})

def jenis(request, appmenu):
    data_jenis_list = ModuleService.jenis_list()
    return render(request, 'app/data-jenis.html', {'data_jenis_list':data_jenis_list})

def usergroup(request,appmenu):
    group_list = ModuleService.usergroup_list()
    return render(request, 'app/cms-group.html',{'group_list':group_list})
def category(request, appmenu):
    category_list = ModuleService.category_list()
    return render(request, 'app/category.html',{'category_list':category_list})

def appmodule(request, appmenu):
    appmodule_list = ModuleService.appmodule_list()
    return render(request, 'app/module.html',{'appmodule_list':appmodule_list})

def dashboardtangsel(request, appmenu):
    return render(request, 'app/dashboardtangsel.html')

def data_pariwisata(request, appmenu):
    category =ModuleService.get_master_category_by_menutext_id(appmenu.menutext_id)
    # if category:
    #     print("category ",category.categoryname)
    list_tourism=[]
    if category:
        list_tourism =ModuleService.get_list_data_pariwisata(category.categoryname)
    return render(request, 'app/data-wisata.html', {'list_tourism':list_tourism, 'category':category, 'appmenu':appmenu})
    # return render(request, 'app/data-wisata.html', {'list_tourism':None, 'category':None})

def add_data_pariwisata(request,appmenu,categoryname):
    category = ModuleService.get_master_category_by_name(categoryname)
    return render(request, 'app/add-data-wisata.html',{'category':category})

def statistik_pariwisata(request, appmenu):
    module_name = appmenu.module.modulename
    category_name = module_name.replace("data","")
    
    data_tourisms = ModuleService.get_list_data_tourist_by_categoryname(category_name)
    return render(request,'app/statistik-pariwisata.html',{'data_tourisms':data_tourisms, 'category_name':category_name,'appmenu':appmenu})


    
# def jasamakanan(request):
#     return render(request, 'app/data-wisata.html')