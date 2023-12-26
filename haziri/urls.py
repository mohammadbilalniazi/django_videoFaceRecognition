from django.urls import path
from . import views_haziri
from . import biometri_haziri

urlpatterns = [
    path('controller/haziri/<mudeeriath_id>/<start_date>/',views_haziri.controller_haziri),
    path('monthly_haziri/form/',views_haziri.haziri_form),
    path('daily_haziri/form/',biometri_haziri.daily_haziri_form),
    path('monthly_haziri/',views_haziri.form_save),
    path('export_excel/',views_haziri.haziri_export_excel,name="haziri_export_excel"),
    path('daily_haziri/report/<mudeeriath_id>/<user>/<year>/<month>',biometri_haziri.daily_haziri_report),    
    path('daily_haziri/report',biometri_haziri.daily_haziri_report),
]
