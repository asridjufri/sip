from django.urls import path
from django.conf.urls import url
from app.views import backoffice, dispatcher,dashboard
from django.contrib.auth.decorators import login_required
urlpatterns = [
    
    url(r'^menus$',backoffice.menu, name='menus'),
    url(r'^login$',backoffice.CustomLoginView.as_view(), name='login-page'),
    url(r'^logout$',login_required(backoffice.CustomLogoutView.as_view()), name='logout-page'),
    url(r'^home$',backoffice.home, name='home-page'),
    url(r'^$',dispatcher.dispatcher, name='dispatcher'),
    
    url(r'^data-jenis$',backoffice.data_jenis, name='data-jenis'),
    url(r'^cms-groups$',backoffice.groups, name='cms-groups'),
    url(r'^slides/$',dashboard.ListSlide.as_view(), name='list-slide'),

    url(r'^slide/add/$', dashboard.CreateSlide.as_view(), name='add-slide'),
    url(r'^slide/edit/(?P<pk>\d+)/$', dashboard.UpdateSlide.as_view(), name='edit-slide'),
    url(r'^slide/delete/(?P<pk>\d+)/$', dashboard.DeleteSlide.as_view(), name='delete-slide'),
    url(r'^dashboards/$',dashboard.ListDashboard.as_view(), name='list-dashboard'),
    url(r'^dashboard/add/$', dashboard.CreateDashboard.as_view(), name='add-dashboard'),
    url(r'^dashboard/edit/(?P<pk>\d+)/$', dashboard.UpdateDashboard.as_view(), name='edit-dashboard'),
    url(r'^dashboard/delete/(?P<pk>\d+)/$', dashboard.DeleteDashboard.as_view(), name='delete-dashboard'),
    url(r'^images/$',dashboard.ListImage.as_view(), name='list-image'),
    url(r'^image/add/$', dashboard.CreateImage.as_view(), name='add-image'),
    url(r'^image/edit/(?P<pk>\d+)/$', dashboard.UpdateImage.as_view(), name='edit-image'),
    url(r'^image/delete/(?P<pk>\d+)/$', dashboard.DeleteImage.as_view(), name='delete-image'),
    url(r'^videos/$',dashboard.ListVideo.as_view(), name='list-video'),
    url(r'^video/add/$', dashboard.CreateVideo.as_view(), name='add-video'),
    url(r'^video/edit/(?P<pk>\d+)/$', dashboard.UpdateVideo.as_view(), name='edit-video'),
    url(r'^video/delete/(?P<pk>\d+)/$', dashboard.DeleteVideo.as_view(), name='delete-video'),
    url(r'^excels/$',dashboard.ListExcel.as_view(), name='list-excel'),
    url(r'^excel/add/$', dashboard.CreateExcel.as_view(), name='add-excel'),
    url(r'^excel/delete/(?P<pk>\d+)/$', dashboard.DeleteExcel.as_view(), name='delete-excel'),
    url(r'^excel/import/$', dashboard.import_excel_data, name='import-excel'),
    url(r'^excel/logs/$', dashboard.import_excel_log, name='log-excel'),
    
    

    # url(r'^ajax/chart/tourism-pendapatan$',dashboard.tourism_vs_pendapatan, name='ajax-chart-tourism-pendapatan'),
    # url(r'^ajax/chart/tourism-pendapatan-annual$',dashboard.tourism_vs_pendapatan_annually, name='ajax-chart-tourism-pendapatan-annual'),
    # url(r'^ajax/chart/tourism-pendapatan-monthly$',dashboard.tourism_vs_pendapatan_monthly, name='ajax-chart-tourism-pendapatan-monthly'),
    

]
