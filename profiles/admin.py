from django.contrib import admin
from .models import Profile
from django.utils.html import format_html

# Register your models here.

@admin.register(Profile)
class profileAdmin(admin.ModelAdmin):
    def user_image(self,obj):
        if hasattr(obj,'photo'):
            return format_html("<img src='/media/{}'/>".format(obj.photo))
        else:
            return ""
    list_display=("user","uuid","user_image")