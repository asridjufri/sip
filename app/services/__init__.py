
from app.models import Appmenu, Appgroup, Appuser, Appmodule
from app.models import MasterJenis, MasterCategory, MasterTourism, DataTourist
from app import repository
import json
class MenuService():
    @staticmethod
    def get_allowed_menus(username):
        appuser = Appuser.objects.filter(user=username, deleted=0).first()
        appgroup = Appgroup.objects.filter(groupid=appuser.groupid, deleted=0).first()
        print(appgroup)
        menu_str = appgroup.menusid
        menus = menu_str.split("**")
        cleaned_menu=[]
        ordered_menu={}
        array_ordered_menu=[]
        for menu in menus:
            cleaned_menu.append(menu.replace("*",""))
        allowed_menu = Appmenu.objects.filter(menuid__in=cleaned_menu, deleted=0,module__deleted=0).order_by('menuorder')
        for menu in allowed_menu:
            if menu.parentid is None:
                if str(menu.menuid) in ordered_menu:
                    ordered_menu[str(menu.menuid)]['menutext']=menu.menutext
                    ordered_menu[str(menu.menuid)]['modulename']=menu.module.modulename
                else:
                    ordered_menu[str(menu.menuid)]={'menutext':menu.menutext,'modulename':menu.module.modulename, 'childs':[],'has_child':False}
            else:
                if str(menu.parentid) in ordered_menu:
                    ordered_menu[str(menu.parentid)]['childs'].append({'menutext':menu.menutext,'modulename':menu.module.modulename})
                    ordered_menu[str(menu.parentid)]['has_child']=True
                else:
                    ordered_menu[str(menu.parentid)]={'menutext':None, 'modulename':None,'childs':[{'menutext':menu.menutext,'modulename':menu.module.modulename}],'has_child':True}
        for k in ordered_menu:
            array_ordered_menu.append(ordered_menu[k])
        return array_ordered_menu
    
    

class ModuleService():
    @staticmethod
    def jenis_list():
        return MasterJenis.objects.filter(deleted=0)
    
    @staticmethod
    def menu_list():
        menus = Appmenu.objects.filter(deleted=0, module__modulename__isnull=False)
        return menus
    
    @staticmethod
    def usergroup_list():
        group_list = Appgroup.objects.filter(deleted=0)
        return group_list
    @staticmethod
    def category_list():
        categories = MasterCategory.objects.filter(deleted=0)
        return categories

    @staticmethod
    def appmodule_list():
        modules = Appmodule.objects.filter(deleted=0)
        return modules

    @staticmethod
    def get_default_modulename(username):
        user = Appuser.objects.filter(user=username,deleted=0).first()
        group = Appgroup.objects.filter(groupid=user.groupid, deleted=0, defaultmodule__isnull=False).first()
        print(group.defaultmodule)
        return group.defaultmodule.modulename

    @staticmethod
    def get_master_category_by_menutext_id(menutext_id):
        
        return MasterCategory.objects.filter(categoryname = menutext_id, deleted=0).first()

    @staticmethod
    def get_master_category_by_name(categoryname):
        
        return MasterCategory.objects.filter(categoryname = categoryname, deleted=0).first()
        
    @staticmethod
    def get_menu_by_module_name(module_name):
        module = Appmodule.objects.filter(modulename=module_name, deleted=0).first()
        return Appmenu.objects.filter(module=module).first()
    @staticmethod
    def get_menu_by_menuid(menuid):
        return Appmenu.objects.filter(menuid=menuid).first()

    @staticmethod
    def get_list_data_pariwisata(categoryname):
        return MasterTourism.objects.filter(categoryid=categoryname)

    @staticmethod 
    def get_master_tourism_by_categoryname(categoryname):
        master_tourism = MasterTourism.objects.filter(categoryid=categoryname, deleted=0).first()
        return master_tourism

    @staticmethod
    def get_list_data_tourist_by_master_tourism(master_tourism):
        
        return DataTourist.objects.filter(tourismid=master_tourism.tourismid, deleted=0)
    @staticmethod
    def get_list_data_tourist_by_categoryname(categoryname):
        return DataTourist.objects.filter(tourism__categoryid=categoryname)

        



class DashboardService():
    @staticmethod
    def get_tourism_vs_pendapatan():
        return repository.get_tourisme_vs_pendapatan()
    
    @staticmethod
    def get_tourism_vs_pendapatan_annualy():
        return repository.get_tourisme_vs_pendapatan_annualy()
    
    @staticmethod
    def get_tourism_vs_pendapatan_monthly():
        return repository.get_tourisme_vs_pendapatan_monthly()
    
    @staticmethod
    def get_tourism_vs_wisatawan():
        return repository.get_tourism_vs_wisatawan()
    
    @staticmethod
    def get_tourism_vs_wisatawan_annualy():
        return repository.get_tourism_vs_wisatawan_annualy()
    


