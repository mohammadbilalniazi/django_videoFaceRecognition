from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

def get_model_fields(model):
    field_list=[field.name for field in model._meta.get_fields()]
    return field_list

@admin.register(Languages)
class LanguagesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("id","language","description")
    
@admin.register(Language_Detail)
class Language_DetailAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("id","language","key","value","page")
    list_filter=("language","key","value")
    
@admin.register(Assign_Languages)
class Assign_LanguagesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=("languages","user")
    list_filter=("languages","user")

@admin.register(NawaSanad)
class NawaSanadAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_filter=("nawa_sanad","nawa_sanad_code")

@admin.register(Currency)
class CurrencyAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_filter=("name","applicationid",)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display=("location_code","location_name","location_contact","location_email")



    
    

    
