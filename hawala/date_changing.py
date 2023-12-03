from datetime import datetime
import pytz
from hijri_converter import Gregorian
from jalali_date import  date2jalali
from django.http import JsonResponse
import json
import re
def more_days_month_solut(date_time):
    date_time=str(date_time)
    pattern=r"[\t\n\s]*"
    date_time=re.sub(pattern,"",date_time)
    try:
        date_list=date_time.split("-")
        # print("date_list=",date_list)
        y=date_list[0]
        m=date_list[1]
        d=date_list[2]
        new_date=datetime(int(y),int(m),int(d))
    except:
        date_list=date_time.split("-")
        y=date_list[0]
        m=date_list[1]
        d=date_list[2]
        d=int(d)-1
    try:    
        new_date=datetime(int(y),int(m),int(d))
        
    except ValueError:
        d=int(d)-1
        try:
            new_date=datetime(int(y),int(m),int(d))
        except ValueError:
            d=int(d)-1
            new_date=datetime(int(y),int(m),int(d))

    return new_date.date()
 
def more_days_month_sol_datetime(date_time):
    try:
        date_time_lis=date_time.split(" ")
        time=date_time_lis[-1]
        time_list=time.split(":")
        date=date_time_lis[0]  
        date_list=date.split("-")
        y=date_list[0]
        m=date_list[1]
        d=date_list[2]
        H=time_list[0]
        M=time_list[1]
        S=time_list[2]
        new_date=datetime(int(y),int(m),int(d))
        # print("datetime@@@@@@@@@@@=Year",y," m=",m," d=",d," H=",H," M=",M," S=",S)
    except:
        d=int(d)-1
    try:
        new_date=datetime(int(y),int(m),int(d),int(H),int(M),int(S))
        return new_date
    except ValueError:
        d=int(d)-1
        try:
            new_date=datetime(int(y),int(m),int(d),int(H),int(M),int(S))
            return new_date
        except ValueError:
            d=int(d)-1
            new_date=datetime(int(y),int(m),int(d),int(H),int(M),int(S))
            return new_date  
        
def date_to_qamari(request):
    if request.method=="POST":
        print(request.POST)
        print("request.POST['date_controll']=",request.POST.get('date_controll',None))
        print("request.POST['date_hawala']=",request.POST.get('date_hawala',None))
        #return HttpResponse("test shamsi")
        date=pytz.timezone('Asia/Kabul').localize(datetime.now()).strftime("%Y-%m-%d")
        date_miladi=datetime.strptime(date,"%Y-%m-%d")
        date_shamsi=date2jalali(date_miladi)
        y=datetime.now().strftime('%Y')
        m=datetime.now().strftime('%m')
        d=datetime.now().strftime('%d')
        date_qamari=Gregorian(int(y),int(m),int(d)).to_hijri()
        data={'shamsi':str(date_shamsi),'miladi':str(date_miladi),'qamari':str(date_qamari)}
        print(data)
        return JsonResponse(json.dumps(data), safe=False)
    
    date=pytz.timezone('Asia/Kabul').localize(datetime.now()).strftime("%Y-%m-%d")
    date_miladi=datetime.strptime(date,"%Y-%m-%d")
    date_shamsi=date2jalali(date_miladi)
    
    return JsonResponse(json.dumps(date_shamsi, indent=4, sort_keys=True, default=str) ,safe=False)


def date_to_shamsi(request):
    if request.method=="POST":
        
        data_from_post = json.load(request)
        print("data_from_post=",data_from_post)
        print("data_from_post[date_hawala]=",data_from_post["date_hawala"])
        # print(request.POST)
        # print("request.POST['date_hawala']=",request.POST.get('date_hawala',None))
        #shamsi=request.POST.get('date_controll',None)
        miladi=data_from_post["date_hawala"]
        #return HttpResponse("test shamsi")
        #date=pytz.timezone('Asia/Kabul').localize(datetime.now()).strftime("%Y-%m-%d")
        date_miladi_timzone=pytz.timezone('Asia/Kabul').localize(datetime.strptime(miladi,"%Y-%m-%d"))
        date=date_miladi_timzone.strftime("%Y-%m-%d")
        date_miladi=datetime.strptime(date,"%Y-%m-%d")
        date_shamsi=date2jalali(date_miladi)
        y=date_miladi_timzone.strftime('%Y')
        m=date_miladi_timzone.strftime('%m')
        d=date_miladi_timzone.strftime('%d')
        date_qamari=Gregorian(int(y),int(m),int(d)).to_hijri()
        data={'shamsi':str(date_shamsi),'miladi':str(date_miladi.strftime("%Y-%m-%d")),'qamari':str(date_qamari)}
        print(data)
        return JsonResponse(json.dumps(data), safe=False)
    
    return JsonResponse(None)
 

def current_date():
   
    date_miladi=pytz.timezone('Asia/Kabul').localize(datetime.now()).strftime("%Y-%m-%d")
    date_miladi_obj=datetime.strptime(date_miladi,"%Y-%m-%d")
    date_shamsi=date2jalali(date_miladi_obj)
    date_shamsi=str(date_shamsi)
    y=datetime.now().strftime('%Y')
    m=datetime.now().strftime('%m')
    d=datetime.now().strftime('%d')

    date_qamari=Gregorian(int(y),int(m),int(d)).to_hijri()
    date_qamari=str(date_qamari)
    # print("date_shamsi,date_qamari,date_miladi ",date_shamsi," ",date_qamari," ",date_miladi)
    return (date_shamsi,date_qamari,date_miladi) #all strings


def current_shamsi_date():
   
    date_miladi=pytz.timezone('Asia/Kabul').localize(datetime.now()).strftime("%Y-%m-%d")
    date_miladi_obj=datetime.strptime(date_miladi,"%Y-%m-%d")
    date_shamsi=date2jalali(date_miladi_obj)
    date_shamsi=str(date_shamsi)
    # fisclayear=datetime.now().strftime('%Y')
    # print("date_shamsi,date_qamari,date_miladi ",date_shamsi," ",date_qamari," ",date_miladi)
    return date_shamsi #all strings