from django.urls import path
from . import views_haziri
from . import biometri_haziri

urlpatterns = [
   
    path('controller/haziri/<mudeeriath_id>/<start_date>/<end_date>/',views_haziri.controller_haziri),
    path('haziri_details/form/',views_haziri.haziri_form),
    path('daily_haziri/form/',biometri_haziri.daily_haziri_form),
    path('haziri_details/',views_haziri.form_save),
    path('export_excel/',views_haziri.haziri_export_excel,name="haziri_export_excel"),
]
