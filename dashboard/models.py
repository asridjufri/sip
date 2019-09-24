from django.db import models

# # Create your models here.
class Dashboard(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=1024)
    default_duration= models.IntegerField(default=10000)
    running_text = models.TextField(default='-')
    def __str__(self):
        return self.name

SLIDE_TYPES=(("iframe","iframe"), ("image","image"),("video","video"),("simple_text","simple text"),("quotes","quotes"),("html","html"))
class Slide(models.Model):
    title = models.CharField(max_length=255)
    slide_type = models.CharField(default="iframe",choices=SLIDE_TYPES,max_length=25)
    duration = models.IntegerField(default=0)
    data_string = models.CharField(max_length=2045)
    order = models.IntegerField()
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class ImageGallery(models.Model):
    title = models.CharField(max_length=25)
    img_file = models.ImageField(upload_to='imgs/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class VideoGallery(models.Model):
    title = models.CharField(max_length=25)
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class ExcelFiles(models.Model):
    title = models.CharField(max_length=25)
    category= models.CharField(max_length=25)
    year= models.IntegerField()
    excel_file = models.FileField(upload_to='excels/')
    upload_log = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    


    
