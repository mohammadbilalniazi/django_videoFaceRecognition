from .models import Daily_Haziri
from django.template import loader
from django.http import HttpResponse
from logs.models import Log
from hawala.date_changing import current_shamsi_date
from datetime import datetime
from hawala.models import Controller,Mudeeriath

def daily_haziri_form(request):
    context={}
    template=loader.get_template("haziri/daily_haziri.html")
    return HttpResponse(template.render({},request))


def daily_haziri_report(request,mudeeriath_id=None):
    context={}
    current=current_shamsi_date()
    current_Y_m_d=current.split('-')
    initial_date_str=current_Y_m_d[0]+'-'+current_Y_m_d[1]+'-01'
    initial_date=datetime.strptime(initial_date_str,'%Y-%m-%d')
    current_date=datetime.strptime(current,'%Y-%m-%d')
    print("initial_datetime ",initial_date," current_datetime ",current_date)
    logs=Log.objects.filter(date__range=[initial_date,current_date])
    if mudeeriath_id!=None: 
        # controllers=Controller.objects.filter(mudeeriath__id=mudeeriath_id)
        logs=logs.filter(profile__user__controller__mudeeriath__id=mudeeriath_id)
    mudeeriaths=Mudeeriath.objects.all()
    print("logs ",logs," mudeeriaths ",mudeeriaths)
    context['logs']=logs
    context['mudeeriaths']=mudeeriaths
    template=loader.get_template("haziri/report_daily_haziri.html")
    return HttpResponse(template.render(context,request))