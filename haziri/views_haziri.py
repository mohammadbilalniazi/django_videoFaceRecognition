import re
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from datetime import datetime #,date 
from django.contrib import messages
from jalali_date import date2jalali,datetime2jalali
# from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
from django.contrib.auth.decorators import login_required,permission_required
from .serializers import Haziri_Serializer,Monthly_Haziri_Serializer,ControllerHaziriSerializer
from hawala.date_changing import more_days_month_solut,current_shamsi_date
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions

from .models import Monthly_Haziri,Haziri
from hawala.models import Mudeeriath,Controller
from hawala.views_hawala import get_mudeeriath
from .forms import HaziriForm     
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import xlwt
import requests
import json
from django.forms.models import model_to_dict
from configuration.models import Languages
@login_required(login_url='/') 
@permission_required('hawala.view_hawala',login_url='/admin')
def haziri_export_excel(request):
    start_date=request.POST.get("start_date",None)
    end_date=request.POST.get("end_date",None)
    month=request.POST.get("month","all")
    mudeeriath_id=request.POST.get("mudeeriath","all")
    base_url="{0}://{1}".format(request.scheme,request.get_host())
    if not request.user.is_superuser: # we should only get haziri of specific mudeeriath
        from hawala.views_hawala import get_mudeeriath
        query_mudeeriath=get_mudeeriath(request)
        mudeeriath_id=str(query_mudeeriath[0].id)
     
    response=requests.get(str(base_url)+"/haziri/controller/haziri/"+mudeeriath_id+"/"+start_date+"/"+end_date+"/")
    # response=controller_haziri(request,mudeeriath,start_date,end_date)
    months_islamic_list=['حمل','ثور','جوزا','سرطان','اسد','سنبله','میزان','عقرب','قوس','جدی','دلو','حوت']
    print("data=",response.status_code)# 200
    raw_data=response.content
    # print("response.content=",raw_data)
    pure_data=raw_data.decode("utf-8") # string
    pure_data=json.loads(pure_data) #change string to dict
    # print("pure_data ",pure_data)
    # print(" type(pure_data) ",type(pure_data) )
    # print(" type(pure_data[0]) ",type(pure_data[0]) )
    for index in range(len(pure_data)):
        dic=pure_data[index]
        # print("dic=",dic)
        keys=dic.keys()
        break
    columns=[]
    for k in keys:
        columns.append(k)
    columns.reverse()
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment;filename='+str(datetime.now())+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet(datetime.now().strftime('%Y-%m-%d'))      
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True
    font_style=xlwt.XFStyle()  

    language_dict={}
    language_dict={"first_name":["اسم"],"father_name":["ولد"],"qadam":["قدم"],"mudeeriath_name":["وزارت"],"wazeefa":["وظیفه"],"basth":["بست"],"kaifyath_haziri":["ملاحظات"],"report_date":["تاریخ"],"total_present":["حاضر"],"total_absent":["غیرحاضر"],"total_leave":["رقعه"],"month":["برج"],"total_tafrihi":["تفریحی"],"total_zaroori":["ضروری"],"total_marizi":["مریضی"],"total_hajj":["حچ"],"total_waladi":["ولادی"],"id":["#"]}  
    
    def get_width(num_characters):
        return int((1+num_characters) * 256)
    excel_col=0
    for col_num in range(len(columns)):      
        if columns[col_num] not in ["user_name","monthly_haziri_status","haziri_status","user_id","mudeeriath_id","is_haziri_uploaded"]:
            xpattern = xlwt.Pattern()
            xpattern.pattern = 0x01
            xpattern.pattern_fore_colour =xlwt.Style.colour_map['black']         
            xfont = xlwt.Font()
            xfont.colour_index=xlwt.Style.colour_map['white']
            xfont.bold = True          #  bold 
            xfont.height = 16 * 12  
            font_style.font=xfont
            font_style.pattern=xpattern
            ws.write(row_num,excel_col,language_dict[columns[col_num]][0],font_style)
            ws.col(excel_col).width=get_width(len(str(columns[col_num]))+10)
            excel_col=excel_col+1
    
    for index in range(len(pure_data)):
        row=pure_data[index]
        # print("len(rows)=",len(row)," row=",row,"\n")
        excel_col=0
        for col_num in range(len(columns)):
            xpattern = xlwt.Pattern()
            xpattern.pattern = 0x01
            xpattern.pattern_fore_colour =xlwt.Style.colour_map['white']         
            font_style.pattern=xpattern
            xfont = xlwt.Font()
            xfont.colour_index =xlwt.Style.colour_map['blue']    #  set font color 
            xfont.bold = True          #  bold 
            xfont.height = 18 * 16       
                   
            font_style.font=xfont
            key=columns[col_num]
            #############value handling#############
            if key=="month":
                value=months_islamic_list[int(row[key])-1] # if row['month']==12 then index is 11 
            else:
                value=row[key]
                
            if key not in ["user_name","monthly_haziri_status","haziri_status","user_id","mudeeriath_id","is_haziri_uploaded"]:
                if key=="is_haziri_uploaded":
                    if value==False:                 
                        xpattern = xlwt.Pattern()
                        xpattern.pattern = 0x01
                        xpattern.pattern_fore_colour =xlwt.Style.colour_map['red']
                        
                        xfont = xlwt.Font()
                        xfont.colour_index=xlwt.Style.colour_map['black']
                        xfont.bold = True          #  bold 
                        xfont.height = 18 * 16  
                        font_style.font=xfont
                        font_style.pattern=xpattern

                if key=="mudeeriath_name":
                    xpattern = xlwt.Pattern()
                    xpattern.pattern = 0x01
                    xpattern.pattern_fore_colour =xlwt.Style.colour_map['white']
                    
                    xfont = xlwt.Font()
                    xfont.colour_index=xlwt.Style.colour_map['black']
                    xfont.bold = True          #  bold 
                    xfont.height = 20 * 18  
                    font_style.font=xfont
                    font_style.pattern=xpattern
                ws.write(row_num+1,excel_col,value,font_style)
                # ws.col(col_num).width=get_width(len(str(value)))
                ws.col(excel_col).width=get_width(len(str(key)))
                excel_col=excel_col+1
                    
        row_num=row_num+1
    wb.save(response) 
    return response

@login_required(login_url='/')
@permission_required('haziri.view_haziri',login_url='/admin')
def haziri_form(request,haziri_id=None):
    context={}
    context["mudeeriaths"]=get_mudeeriath(request)
    context["form_start_end_date"]=HaziriForm()
    # from hawala.permissions import has_permission
    # context=has_permission(request,context)
    context["languages"]=Languages.objects.all().distinct()
    template=loader.get_template('haziri/haziri.html') #haziri_temp_8_22.html
    if haziri_id!=None:         #update
        context={
            'haziri':Monthly_Haziri.objects.filter(id=int(haziri_id))
        } 
    context["languages"]=Languages.objects.all().distinct()   
    return HttpResponse(template.render(context,request))


# @login_required(login_url='/')
#@permission_required('hawala.add_kitabkhana',login_url='/admin')
@api_view(['POST'])
def form_save(request): 
    ###############################################branch1###############################
    #[{'user_id': '10', 'mudeeriath': '4', 'total_present': '1', 'month': '06', 'total_absent': '1', 'total_leave': '1', 'report_date': '1401-06-02'}] lenth 1 request.data[0]['user_id']
    haziri_report_data=[]
    ################################################### end Branch 1###############
    print("request.data=",request.data," current_shamsi_date() ",current_shamsi_date())
    # print("test1")
    fiscalyear=current_shamsi_date().split("-")[0]
    haziri_query=Haziri.objects.filter(mudeeriath=request.data['mudeeriath'],month=request.data['month'],fiscalyear=int(fiscalyear))
    if haziri_query.count()>0:    
        validated_data=request.data
        haziri_report_set =validated_data.pop('monthly_haziri_set') # it is list of dict detail haziri
        haziri_obj=haziri_query[0]
        print("haziri_query=",haziri_query)
        # ######################################################Update############################
        for dict_haziri_detail in haziri_report_set:
            user_id=dict_haziri_detail['user_id']
            user_id=User.objects.get(id=int(user_id))
            haziri_detail_query=Monthly_Haziri.objects.filter(haziri=haziri_obj,user_id=user_id)
                    
            print("validated_data=",validated_data)
            print("haziri_report_set=",haziri_report_set)
            if haziri_detail_query.count()>0:
                haziri_detail_obj=haziri_detail_query[0]
                print("***********dict_haziri_detail['kaifyath_haziri']",dict_haziri_detail['kaifyath_haziri'])
                haziri_detail_obj.kaifyath_haziri=dict_haziri_detail['kaifyath_haziri']
                
                haziri_detail_obj.total_present=dict_haziri_detail['total_present']
                haziri_detail_obj.total_absent=dict_haziri_detail['total_absent']
                haziri_detail_obj.total_leave=dict_haziri_detail['total_leave']
                
                haziri_detail_obj.total_tafrihi=dict_haziri_detail['total_tafrihi']
                haziri_detail_obj.total_zaroori=dict_haziri_detail['total_zaroori']
                haziri_detail_obj.total_waladi=dict_haziri_detail['total_waladi']
                
                haziri_detail_obj.total_hajj=dict_haziri_detail['total_hajj']
                haziri_detail_obj.total_marizi=dict_haziri_detail['total_marizi']
                haziri_detail_obj.status=dict_haziri_detail['status']
                try:
                    haziri_detail_obj.save()
                except Exception as e:
                    pass
            else:
                dict_haziri_detail['user_id']=User.objects.get(id=dict_haziri_detail['user_id'])
                Monthly_Haziri.objects.create(haziri=haziri_obj,**dict_haziri_detail)
        
        return Response("haziri_detail_created", status=status.HTTP_201_CREATED)
        #update

        #print("Haziri_details_set.all() ",haziri_obj.monthly_haziri_set.all())
    # ######################################################New Haziri Creation############################
    serializer=Haziri_Serializer(data=request.data)
    #print("serializer=",serializer)
    if serializer.is_valid():
        print("serializer.validated_data=",serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print("ERROR")
        print(serializer.errors)     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(('GET',))
# @permission_classes((permissions.allowAny))
def haziri_show(request,mudeeriath_id=None):
    if request.method=="GET":
        if mudeeriath_id==None: ####################mudeeriath maybe id or name i will check
            query_set=Monthly_Haziri.objects.all().order_by('-pk')
        else:
            query_set=Monthly_Haziri.objects.filter(mudeeriath=int(mudeeriath_id)).order_by('-pk')
        serializer=Monthly_Haziri_Serializer(query_set,many=True) 
        #print("serializer.data user=",serializer.data)
        #return HttpResponse(serializer.data)
        return Response(serializer.data)
    else:
        return Response("Not acceptable request")



@api_view(('GET',))
def controller_haziri(request,mudeeriath_id="all",start_date="1401-01-01"):
    start_date=more_days_month_solut(start_date)
    # end_date=more_days_month_solut(end_date)
    #return HttpResponse(mudeeriath_id)
    if mudeeriath_id=="all": ####################mudeeriath maybe id or name i will check
        query_set=Controller.objects.all().order_by('mudeeriath')
    else:
        query_mudeeriath=Mudeeriath.objects.filter(id=int(mudeeriath_id))  
        query_set=Controller.objects.filter(mudeeriath=query_mudeeriath[0]).order_by('mudeeriath')  
    context={"start_date":start_date}
    #  context={"start_date":start_date,"end_date":end_date}
    serializer=ControllerHaziriSerializer(query_set,many=True,context=context) 
    # print("controllerSerializer.data=",serializer.data)
    #print(Response(serializer.data))
    return Response(serializer.data)  