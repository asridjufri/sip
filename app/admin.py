from django.contrib import admin
from app.models import Appconfiguration, Appgroup, Applang,Appmodule
# Register your models here.
from app.models import Appmenu, Appnotification, Appnotificationuser
from app.models import Appuser

from app.models import MasterCategory, MasterJenis, MasterKecamatan,MasterLanguage
from app.models import MasterTourism

from app.models import DataTourist 

#---- confugration

admin.site.register(Appconfiguration)
admin.site.register(Appgroup)
admin.site.register(Applang)
admin.site.register(Appmodule)

admin.site.register(Appmenu)
admin.site.register(Appnotification)
admin.site.register(Appnotificationuser)
admin.site.register(Appuser)

admin.site.register(MasterCategory)
admin.site.register(MasterJenis)
admin.site.register(MasterKecamatan)
admin.site.register(MasterLanguage)
admin.site.register(MasterTourism)

admin.site.register(DataTourist)