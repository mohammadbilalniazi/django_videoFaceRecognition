from .models import Daily_Haziri
from django.template import loader
from django.http import HttpResponse
from logs.models import FaceLog
from hawala.date_changing import current_shamsi_date
from datetime import datetime
from hawala.models import Mudeeriath
from .models import MONTHS
from django.db.models import Q
from django.contrib.auth.models import User

def daily_haziri_form(request):
    context={}
    template=loader.get_template("haziri/daily_haziri.html")
    return HttpResponse(template.render({},request))


def daily_haziri_report(request,mudeeriath_id=None,user=None,year=None,month=None):
    context={}
    current=current_shamsi_date()
    current_Y_m_d=current.split('-')
    initial_date_str=current_Y_m_d[0]+'-'+current_Y_m_d[1]+'-01'
    initial_date=datetime.strptime(initial_date_str,'%Y-%m-%d')
    current_date=datetime.strptime(current,'%Y-%m-%d')
    print("initial_datetime ",initial_date," current_datetime ",current_date," current ",current," current.split() ",current.split('-'))

    if year==None or month==None:
        year=current.split('-')[0]
        month=current.split('-')[1]
        # logs=FaceLog.objects.filter(date__range=[initial_date,current_date])
        daily_haziries=Daily_Haziri.objects.filter(date__range=[initial_date,current_date])
        # print("initial_date,current_date ",logs)
    else:
        # logs=FaceLog.objects.filter(year=int(year),month=int(month))
        initial_date=datetime.strptime(str(year)+"-"+str(month)+"-01",'%Y-%m-%d')
        last_date=datetime.strptime(str(year)+"-"+str(month)+"-31",'%Y-%m-%d')
        daily_haziries=Daily_Haziri.objects.filter(date__range=[initial_date,last_date])
        # print("year=int(year),month=int(month) ",logs)
    if mudeeriath_id!=None:  
        # logs=logs.filter(profile__user__controller__mudeeriath__id=mudeeriath_id)
        daily_haziries=daily_haziries.filter(user__controller__mudeeriath_id=mudeeriath_id)
    else:
        mudeeriath_id=0

    if user!=None:  
        # logs=logs.filter(profile__user__id=user)
        daily_haziries=daily_haziries.filter(user__id=user)
    else:
        user=request.user.id
    # print("logs ",logs," daily_haziries",daily_haziries)
    
    mudeeriaths=Mudeeriath.objects.all()
    users=User.objects.filter(Q(mudeeriath__id=mudeeriath_id) | Q(controller__mudeeriath__id=mudeeriath_id))
    months=[{"value":month[0],"label":month[1]} for month in MONTHS]
    # print("logs ",logs," mudeeriaths ",mudeeriaths)
    # print("daily_haziries.log.set ",daily_haziries[3].log_set.all())
    # context['logs']=logs
    context['daily_haziries']=daily_haziries
    context['mudeeriath_id']=int(mudeeriath_id)
    context['month']=int(month)
    context['year']=year
    # print("users ",users)
    context['users']=users
    context['user']=int(user)
    context['months']=months
    print("context['month'] ",context['month'])
    context['mudeeriaths']=mudeeriaths
    template=loader.get_template("haziri/report_daily_haziri.html")
    return HttpResponse(template.render(context,request))