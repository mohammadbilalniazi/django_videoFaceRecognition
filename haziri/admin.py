from this import d
from django.contrib import admin
from django.contrib.auth.models import User
from .models import General_Holidays,Haziri,Haziri_Details,Daily_Haziri
from django.shortcuts import redirect



# #######################################extra buttons#####################################'

# from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
# from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
# from django.http import HttpResponse, JsonResponse
# from django.contrib import admin
# from django.views.decorators.clickjacking import xframe_options_sameorigin
# from django.views.decorators.csrf import csrf_exempt

admin.site.register(Daily_Haziri)
admin.site.register(General_Holidays)
admin.site.register(Haziri_Details)
class Haziri_Details_Admin(admin.ModelAdmin):
    list_display=['user_id','total_present','total_absent','total_leave','status','mudeeriath']#,'get_status'
    def mudeeriath(self,obj):
        return obj.haziri.mudeeriath
