from django.shortcuts import render
from app.models import Appmenu, MasterJenis, Appgroup

from django.contrib.auth.views import LoginView, LogoutView

def test(request):
    return render(request,'app/index.html')

def home(request):
    return render(request, 'app/sliders/index.html')

#------- auth handle
class CustomLoginView(LoginView):
	template_name = 'app/login/index.html'
	

class CustomLogoutView(LogoutView):
	pass

def login_page(request):
	return render(request, 'app/login/index.html')

def menu(request):
    menus = Appmenu.objects.filter(deleted=0, module__modulename__isnull=False)
    return render(request, 'app/menu.html',{'menus':menus})

def data_jenis(request):
    data_jenis_list = MasterJenis.objects.filter(deleted=0)
    return render(request, 'app/data-jenis.html', {'data_jenis_list':data_jenis_list})

def groups(request):
    group_list = Appgroup.objects.filter(deleted=0)
    return render(request, 'app/cms-group.html',{'group_list':group_list})


