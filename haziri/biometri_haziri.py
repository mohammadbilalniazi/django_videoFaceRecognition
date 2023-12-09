from .models import Daily_Haziri
from django.template import loader
from django.http import HttpResponse
from logs.models import Log
from hawala.date_changing import current_shamsi_date
from datetime import datetime

def daily_haziri_form(request):
    context={}
    current=current_shamsi_date()
    current_Y_m_d=current.split('-')
    initial_datetime_str=current_Y_m_d[0]+'-'+current_Y_m_d[1]+'-01'+" 00:00:00"
    current_datetime_str=current+" 00:00:00"
    initial_datetime=datetime.strptime(initial_datetime_str,'%Y-%m-%d %H:%M:%S')
    current_datetime=datetime.strptime(current_datetime_str,'%Y-%m-%d %H:%M:%S')
    print("initial_datetime ",initial_datetime," current_datetime ",current_datetime)
    logs=Log.objects.filter(created__range=[initial_datetime,current_datetime])
    print("logs ",logs)
    context['logs']=logs
    template=loader.get_template("haziri/daily_haziri.html")
    return HttpResponse(template.render({},request))
