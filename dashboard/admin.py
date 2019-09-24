from django.contrib import admin
from dashboard.models import Dashboard,Slide,ImageGallery, VideoGallery

# Register your models here.
admin.site.register(Dashboard)
admin.site.register(Slide)
admin.site.register(ImageGallery)
admin.site.register(VideoGallery)
