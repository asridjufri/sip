from django.http import JsonResponse
from app.services import DashboardService
from datetime import datetime
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from dashboard.models import Slide, Dashboard, ImageGallery, VideoGallery, ExcelFiles
from django.http import HttpResponseRedirect
from django.contrib import messages
from app.services.excel_service import ImportExcelService
from django.conf import settings
import os
from django.shortcuts import render

from django.urls import  reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required,'get')
class ListSlide(ListView):
    model = Slide
    paginated_by=10000

    template_name='app/dashboard/list-slide.html'

    def get_queryset(self):
        dashboard_id = self.request.GET.get('id',None)
        queryset = Slide.objects.all()
        if not dashboard_id:
            return queryset
        else:
            return queryset.filter(dashboard_id=dashboard_id)
    def get_context_data(self, **kwargs):
        context = super(ListSlide,self).get_context_data(**kwargs)
        dashboard_id = self.request.GET.get('id',None)
        if dashboard_id:
            dashboard = Dashboard.objects.get(pk=dashboard_id)
            context['dashboard'] = dashboard
        return context

@method_decorator(login_required,'get')
class DeleteSlide(DeleteView):
    model = Slide
    template_name = 'app/delete-confirmation.html'

    def get_success_url(self):
        
        return reverse_lazy('list-slide')
    def get_context_data(self, **kwargs):
        context = super(DeleteSlide, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER') #reverse_lazy('list-slide')
        context['ask'] = 'Anda yakin akan menghapus slide : %s ?' %(context['object'].title)
        return context

@method_decorator(login_required,'get')
class ListDashboard(ListView):
    model = Dashboard
    paginated_by=10000
    template_name = 'app/dashboard/list-dashboard.html'


@method_decorator(login_required,'get')
class UpdateDashboard(UpdateView):
    model = Dashboard
    success_url = reverse_lazy('list-dashboard')
    template_name = 'app/dashboard/add-dashboard.html'
    fields=['name','description','default_duration', 'running_text']

@method_decorator(login_required,'get')
class DeleteDashboard(DeleteView):
    model = Dashboard
    template_name = 'app/delete-confirmation.html'

    def get_success_url(self):
        
        return reverse_lazy('list-dashboard')
    def get_context_data(self, **kwargs):
        context = super(DeleteDashboard, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER') #reverse_lazy('list-slide')
        context['ask'] = 'Anda yakin akan menghapus dashboard : %s ?' %(context['object'].name)
        return context

@method_decorator(login_required,'get')
class CreateDashboard(CreateView):
    model = Dashboard
    success_url = reverse_lazy('list-dashboard')
    template_name = 'app/dashboard/add-dashboard.html'
    fields=['name','description','default_duration', 'running_text']

@method_decorator(login_required,'get')
class ListImage(ListView):
    model = ImageGallery
    paginated_by = 10000
    template_name = 'app/dashboard/list-image.html'

@method_decorator(login_required,'get')
class CreateImage(CreateView):
    model = ImageGallery
    success_url = reverse_lazy('list-image')
    template_name = 'app/dashboard/add-image.html'
    fields = ['title', 'img_file']

@method_decorator(login_required,'get')
class UpdateImage(UpdateView):
    model = ImageGallery
    success_url = reverse_lazy('list-image')
    template_name = 'app/dashboard/add-image.html'
    fields = ['title', 'img_file']

@method_decorator(login_required,'get')
class DeleteImage(DeleteView):
    model = ImageGallery
    template_name = 'app/delete-confirmation.html'

    def get_success_url(self):
        
        return reverse_lazy('list-image')
    def get_context_data(self, **kwargs):
        context = super(DeleteImage, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER') #reverse_lazy('list-slide')
        context['ask'] = 'Anda yakin akan menghapus gambar : %s ?' %(context['object'].title)
        return context

@method_decorator(login_required,'get')
class ListVideo(ListView):
    model = VideoGallery
    paginated_by = 10000
    template_name = 'app/dashboard/list-video.html'

@method_decorator(login_required,'get')
class CreateVideo(CreateView):
    model = VideoGallery
    success_url = reverse_lazy('list-video')
    template_name = 'app/dashboard/add-video.html'
    fields = ['title', 'video_file']

@method_decorator(login_required,'get')
class UpdateVideo(UpdateView):
    model = VideoGallery
    success_url = reverse_lazy('list-video')
    template_name = 'app/dashboard/add-video.html'
    fields = ['title', 'video_file']


@method_decorator(login_required,'get')
class DeleteVideo(DeleteView):
    model = VideoGallery
    template_name = 'app/delete-confirmation.html'

    def get_success_url(self):
        
        return reverse_lazy('list-video')
    def get_context_data(self, **kwargs):
        context = super(DeleteVideo, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER') #reverse_lazy('list-slide')
        context['ask'] = 'Anda yakin akan menghapus video : %s ?' %(context['object'].title)
        return context

@method_decorator(login_required,'get')
class ListExcel(ListView):
    model = ExcelFiles
    paginated_by = 10000
    template_name = 'app/dashboard/list-excel.html'

@method_decorator(login_required,'get')
class CreateExcel(CreateView):
    model = ExcelFiles
    success_url = reverse_lazy('list-excel')
    template_name = 'app/dashboard/add-excel.html'
    fields = ['title', 'excel_file','category', 'year']


@method_decorator(login_required,'get')
class DeleteExcel(DeleteView):
    model = ExcelFiles
    template_name = 'app/delete-confirmation.html'

    def get_success_url(self):
        
        return reverse_lazy('list-excel')
    def get_context_data(self, **kwargs):
        context = super(DeleteExcel, self).get_context_data(**kwargs)
        context['back_url'] = self.request.META.get('HTTP_REFERER') #reverse_lazy('list-slide')
        context['ask'] = 'Anda yakin akan menghapus excel : %s ?' %(context['object'].title)
        return context

@method_decorator(login_required,'get')
class UpdateSlide(UpdateView):
    model = Slide
    success_url= reverse_lazy('list-slide')
    template_name= 'app/dashboard/add-slide.html'
    fields=['title','slide_type','duration','data_string','order','dashboard']
    def get_success_url(self):
        dashboard_id = self.request.GET.get('id',None)
        if dashboard_id:
            return self.success_url+'?id='+dashboard_id
        return self.success_url
    def get_context_data(self, **kwargs):
        context = super(UpdateSlide,self).get_context_data(**kwargs)
        dashboard_id = self.request.GET.get('id',None)
        if dashboard_id:
            dashboard = Dashboard.objects.get(pk=dashboard_id)
            context['dashboard'] = dashboard
        else:
            dashboads = Dashboard.objects.all()
            context['dashboards'] = dashboads
        obj = self.object
        slide_type=self.request.GET.get('type',obj.slide_type)

        
        if slide_type == 'image':
            context['images'] = ImageGallery.objects.all()

        elif slide_type == 'video':
            context['videos']= VideoGallery.objects.all()
        context['slide_type'] = slide_type
        return context

@method_decorator(login_required,'get')
def import_excel_data(request):
    excel_id = request.GET.get('id', None)
    exc = ExcelFiles.objects.get(pk=excel_id)
    file = os.path.join(settings.MEDIA_ROOT,exc.excel_file.path)
    msg=""
    try:
        data = ImportExcelService.parse_data(file)
        print(data)
        force=False
        msg=ImportExcelService.save_data(exc.year, exc.category, data,force)
        exc.upload_log="========= SUCCESS IMPORT DATA ==== "
        exc.upload_log+= "\n%s"%msg
        exc.save()
        messages.success(request,exc.upload_log)
    except Exception as e:
        exc.upload_log=str(e)
        exc.upload_log+="\n%s"%msg
        messages.error(request,exc.upload_log)
        exc.save()
    

    return HttpResponseRedirect(reverse_lazy('list-excel'))

@method_decorator(login_required,'get')
def import_excel_log(request):
    excel_id = request.GET.get('id',None)
    exc = ExcelFiles.objects.get(pk=excel_id)
    return render(request, 'app/dashboard/import-log.html',{'excel':exc})


@method_decorator(login_required,'get')
class CreateSlide(CreateView):
    model = Slide
    success_url= reverse_lazy('list-slide')
    template_name= 'app/dashboard/add-slide.html'
    fields=['title','slide_type','duration','data_string','order','dashboard']

    def get_success_url(self):
        dashboard_id = self.request.GET.get('id',None)
        if dashboard_id:
            return self.success_url+'?id='+dashboard_id
        return self.success_url
    def get_context_data(self, **kwargs):
        context = super(CreateSlide,self).get_context_data(**kwargs)
        dashboard_id = self.request.GET.get('id',None)
        if dashboard_id:
            dashboard = Dashboard.objects.get(pk=dashboard_id)
            context['dashboard'] = dashboard
        else:
            dashboads = Dashboard.objects.all()
            context['dashboards'] = dashboads
        slide_type=self.request.GET.get('type','image')

        
        if slide_type == 'image':
            context['images'] = ImageGallery.objects.all()
            
        elif slide_type == 'video':
            context['videos']= VideoGallery.objects.all()
        context['slide_type'] = slide_type
        return context

# def tourism_vs_pendapatan(request):
#     data = DashboardService.get_tourism_vs_pendapatan()
#     jdata = {'title': 'Total Pendapatan Per Kategory Jasa', 'name':'Pendapatan','data':[ ]}
#     for item in data:
#         jdata['data'].append({'name':item['categoryid'],'y':item['pendapatan']})
#     return JsonResponse(jdata)

# def tourism_vs_pendapatan_annually(request):
#     data = DashboardService.get_tourism_vs_pendapatan_annualy()
#     tmp_dict ={}
#     jdata={'title':'Total Pendapatan Per Katogori Jasa Pertahun', 'nama':'Pendapatan', 'series':[]}
#     for item in data:
#         # y = datetime(item['year'],1,1)
#         # y = y.strftime("%Y-%m-%d")
#         # y = int(y.strftime("%s")) 
#         y=item['year']
#         if item['categoryid'] in tmp_dict:
#             tmp_dict[item['categoryid']]['data'].append([y,item['pendapatan']])
#         else:
#             tmp_dict[item['categoryid']] = {'data':[[y,item['pendapatan']]]} 
    
#     for k in tmp_dict:
#         jdata['series'].append({'name':k, 'data':tmp_dict[k]['data']})
#     return JsonResponse(jdata)

# def tourism_vs_pendapatan_monthly(request):
#     data = DashboardService.get_tourism_vs_pendapatan_monthly()
#     tmp_dict ={}
#     jdata={'title':'Total Pendapatan Per Katogori Jasa Bulan', 'nama':'Pendapatan', 'series':[]}
#     for item in data:
#         y = item['date']
#         # y = y.strftime("%Y-%m-%d")
#         # y = int(y.strftime("%s")) 
#         # y=item['year']
#         if item['categoryid'] in tmp_dict:
#             tmp_dict[item['categoryid']]['data'].append([y,item['pendapatan']])
#         else:
#             tmp_dict[item['categoryid']] = {'data':[[y,item['pendapatan']]]} 
    
#     for k in tmp_dict:
#         jdata['series'].append({'name':k, 'data':tmp_dict[k]['data']})
#     return JsonResponse(jdata)

# def tourism_vs_negara_annually(request):
#     data = DashboardService.get_tourism_vs_pendapatan_annualy()
#     tmp_dict ={}
#     jdata={'title':'Total Wistawan Per Negara', 'nama':'Pendapatan', 'series':[]}
#     for item in data:
#         # y = datetime(item['year'],1,1)
#         # y = y.strftime("%Y-%m-%d")
#         # y = int(y.strftime("%s")) 
#         y=item['year']
#         if item['categoryid'] in tmp_dict:
#             tmp_dict[item['categoryid']]['data'].append([y,item['pendapatan']])
#         else:
#             tmp_dict[item['categoryid']] = {'data':[[y,item['pendapatan']]]} 
    
#     for k in tmp_dict:
#         jdata['series'].append({'name':k, 'data':tmp_dict[k]['data']})
#     return JsonResponse(jdata)