from app.views import modules
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.conf import settings
from app.services import ModuleService



def normalize_module_name(modulename,appmenu):
    
    if appmenu:
        if appmenu.parentid is not None:
            parentmenu = ModuleService.get_menu_by_menuid(appmenu.parentid)
            print("------parentmenu")
            print(parentmenu.menutext_id)
            if parentmenu.menutext_id.lower() == "data pariwisata":
                return "data_pariwisata"
            if parentmenu.menutext_id.lower() == "statistik pariwisata":
                return "statistik_pariwisata"


    return modulename.lower()

def dispatcher(request):

    module_name = request.GET.get('module',ModuleService.get_default_modulename('admin'))
    action_name = request.GET.get('action','')
    category = request.GET.get('kategori','')
    appmenu = ModuleService.get_menu_by_module_name(module_name)

    module = normalize_module_name(module_name, appmenu)
    try:
        print("action ",action_name)
        if action_name.lower() == 'add':
            print("action is add")
            module = 'add_%s' %module
        print(module)
        
        module_func = getattr(modules,module)
    except Exception as ex:
        if "'app.views.modules' has no attribute" in str(ex):
            return HttpResponseNotFound("module [%s] not found "%module)
        else:
            if settings.DEBUG:
                return HttpResponseServerError(str(ex))
            else:
                return HttpResponseServerError("opps something error , please contact your administrator")
    
    if action_name == 'add':
        return module_func(request, appmenu,category)
    else:
        return module_func(request, appmenu)

