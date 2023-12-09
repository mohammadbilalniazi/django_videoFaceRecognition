from django.contrib import admin
from .models import Log
from django.utils.html import format_html

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    def show_image(self,obj):
        if hasattr(obj,'photo'):

            return format_html('<img width="150px" height="150px" src="{}"/>'.format(obj.photo.url))
        else:
            return 'no_photo'
    show_image.short_description='Image'
    def show_profile(self,obj):
        if obj.profile!=None:
            return obj.profile.user.username
        else:
            return "No Profile"
    show_profile.short_description='Porfile'
    list_display=('show_profile','photo','date','created','show_image')
# Register your models here.
