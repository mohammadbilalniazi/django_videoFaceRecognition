from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from backup.models import Log
from django.forms.models import model_to_dict
import datetime
import json
from rest_framework import status
from django.urls import reverse
from django.contrib import messages


def select_language(request):
    #user=request.user.username
    context={}
    try:
        user=User.objects.get(username=request.user.username)
   
        
        #print(user.username)
        query_language=Assign_Languages.objects.filter(user=user)
        #print("query_language=",query_language)
        if query_language.count()>0:
            language_obj=query_language[0].languages
            query_keys_lang=Language_Detail.objects.filter(language=language_obj).values_list("key","value")
            context["select_language"]=json.dumps(list(query_keys_lang))
        else:
            context["select_language"]=None   
            
    except Exception as e:
        context["select_language"]=None   
    return JsonResponse(context,safe=True)

def assign_language(request,language):
    #user=request.user.username
    language_query=Languages.objects.filter(language=language)
    user_obj=User.objects.get(username=request.user.username)
    # print("language_query=",model_to_dict(language_query[0]))
    # return HttpResponse(user_obj)
    if language_query.count()>0:
        language_obj=language_query[0]
    else:
        messages.error(request,"No {} Exists!".format(language))
        return HttpResponseRedirect(reverse("hawala_show"))   

    assign_lang_query=Assign_Languages.objects.filter(user=user_obj)
    # print("assign_lang_query ",model_to_dict(assign_lang_query[0]))
    #print("query_language=",query_language)
    if assign_lang_query.count()>0:
        assign_lang_obj=assign_lang_query[0]
        assign_lang_obj.languages=language_obj
    else:
        assign_lang_obj=Assign_Languages(user=user_obj,languages=language_obj) 
    try:
        assign_lang_obj.save()
        m="changed_language"
        messages.success(request,m)
        st=status.HTTP_200_OK
    except Exception as e:
        log_obj=Log(log_type='exception',logger=request.user.username,log_table='Language',log_detail=str(e)+str("47 views_language assign_language.save() problem which has user,language"),log_date=datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'),"%Y-%m-%d")  )
        log_obj.save() 
        m="please see log "
        st=status.HTTP_409_CONFLICT
    # return HttpResponse(user_obj)
    # return JsonResponse({"message":m,"status":st})   
    return HttpResponseRedirect(reverse("hawala_show"))     

def save(request):
    pattern="jalsa"
    query_user_language=Assign_Languages.objects.filter(user=request.user)
    # # print("llist_data =",list_data)
    list_form_data=[{"key":"amiriath_nazarath_wa_hamahangi_controlleran_riasath_muhasibath_label2","language":"pashto"},{"key":"preloader","language":"pashto"},{"key":"status","language":"pashto"},{"key":"wrapper","language":"pashto"},{"key":"amiriath_nazarath_wa_hamahangi_controlleran_riasath_muhasibath_label","language":"pashto"},{"key":"search-wrap","language":"pashto"},{"key":"zuban_label","language":"pashto"},{"key":"jalsa","language":"pashto"},{"key":"jalsa_ilan","language":"pashto"},{"key":"tafseel_jalsa","language":"pashto"},{"key":"payam_rasan_label","language":"pashto"},{"key":"haziri_label","language":"pashto"},{"key":"hawala_label","language":"pashto"},{"key":"thadyath_label","language":"pashto"},{"key":"controller_label","language":"pashto"},{"key":"mudeeriath_label","language":"pashto"},{"key":"kitabkhana_label","language":"pashto"},{"key":"admin_label","language":"pashto"},{"key":"ihsaya_label","language":"pashto"},{"key":"mudeeriaths_ihasaya_div","language":"pashto"},{"key":"mudeeriath","language":"pashto"},{"key":"mudeeriaths_ihasaya_div","language":"pashto"},{"key":"nawasanad","language":"pashto"},{"key":"start_date_div","language":"pashto"},{"key":"start_date_input","language":"pashto"},{"key":"end_date_div","language":"pashto"},{"key":"end_date_input","language":"pashto"},{"key":"money_chart_div","language":"pashto"},{"key":"money_chart","language":"pashto"},{"key":"awayd_sarfajoi_chart_div","language":"pashto"},{"key":"awayd_sarfajoi_chart","language":"pashto"},{"key":"controller_chart_div","language":"pashto"},{"key":"controller_chart","language":"pashto"},{"key":"thadyath_chart_div","language":"pashto"},{"key":"thadyath_chart","language":"pashto"},{"key":"ihsaya_mudeeriath_ha","language":"pashto"},{"key":"","language":"pashto"},{"key":"mudeeriath_label","language":"pashto"},{"key":"mudeeriath_code_label","language":"pashto"},{"key":"majmoa_hawala_label","language":"pashto"},{"key":"detail_label","language":"pashto"},{"key":"pending_label","language":"pashto"},{"key":"mustharadi_controller_label","language":"pashto"},{"key":"majviscont_label","language":"pashto"},{"key":"maj_musthad_thadyath_label","language":"pashto"},{"key":"majchecthad_label","language":"pashto"},{"key":"sarafajoi_label","language":"pashto"},{"key":"majmoa_afghani_label","language":"pashto"},{"key":"majmoa_yuru_label","language":"pashto"},{"key":"majmoa_awayd_label","language":"pashto"},{"key":"ihsaya_mudeeriath_hawalajath","language":"pashto"},{"key":"ihasaya_controllers_label","language":"pashto"},{"key":"controller_label","language":"pashto"},{"key":"mudeeriath_label","language":"pashto"},{"key":"majmoa_hawala_label","language":"pashto"},{"key":"mustharadi_controller_label","language":"pashto"},{"key":"maj_musthad_thadyath_label","language":"pashto"},{"key":"pending_label","language":"pashto"},{"key":"majchecthad_label","language":"pashto"},{"key":"sarafajoi_label","language":"pashto"},{"key":"majmoa_afghani_label","language":"pashto"},{"key":"majmoa_awayd_label","language":"pashto"},{"key":"ihsaya_controllers","language":"pashto"},{"key":"","language":"pashto"},{"key":"mudeeriath_label","language":"pashto"},{"key":"controller_label","language":"pashto"},{"key":"tharikh_controll_label","language":"pashto"},{"key":"mablagh_label","language":"pashto"},{"key":"hawala_no_label","language":"pashto"},{"key":"nawa_sanad_label","language":"pashto"},{"key":"waziath_label","language":"pashto"},{"key":"hawalas","language":"pashto"},{"key":"thadyat_report_label","language":"pashto"},{"key":"","language":"pashto"},{"key":"shumara_label","language":"pashto"},{"key":"code_m16_label","language":"pashto"},{"key":"number_m16_label","language":"pashto"},{"key":"tharikh_m16_label","language":"pashto"},{"key":"controll_qabli_label","language":"pashto"},{"key":"check_thadyath_label","language":"pashto"},{"key":"visa_shuda_label","language":"pashto"},{"key":"mustharad_shuda_label","language":"pashto"},{"key":"waziath_label","language":"pashto"},{"key":"thafseel_label","language":"pashto"},{"key":"thadyath_controll_report","language":"pashto"},{"key":"filhai_sanad_label","language":"pashto"},{"key":"kitabkhana_table","language":"pashto"},{"key":"kitabkhana","language":"pashto"}]
    list_data=list_form_data
    for dict_in_list in list_data:
        key=dict_in_list['key']
        if query_user_language.count()>0:
            if str(key).endswith('_label') or str(key).endswith('_labe') or pattern in str(key):
                obj=Language_Detail(key=key,language=query_user_language[0].languages)
                # print("$$$$inside ",obj)
                try:
                    obj.save()
                    m="saved"
                    st=status.HTTP_200_OK
                    
                except Exception as e:
                    log_obj=Log(log_type='exception',logger=request.user.username,log_table='Language',log_detail=e,log_date=datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'),"%Y-%m-%d")  )
                    log_obj.save() 
                    m="please see log"
                    st=status.HTTP_409_CONFLICT
            else:  
                m="Not accepted label"
                st=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION    
        else:
            m="please see log"
            st=status.HTTP_409_CONFLICT
    return JsonResponse({"message":m,"status":st})



def list_saved_languages(request):
    #user=request.user.username
    context={}
    query_language=Languages.objects.all().values_list("language","description") 
    context["list_saved_languages"]=json.dumps(list(query_language))
    return JsonResponse(context,safe=True)
