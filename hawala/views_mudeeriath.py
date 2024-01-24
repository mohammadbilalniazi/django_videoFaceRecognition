

from django.shortcuts import redirect 
from django.http import HttpResponse
from django.template import loader
from datetime import datetime 
from django.forms.models import model_to_dict
# from jalali_date.fields import JalaliDateField
# from jalali_date.widgets import AdminJalaliDateWidget
# from .forms import HawalaForm
from django.contrib import messages
from jalali_date import date2jalali
# from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
from django.contrib.auth.decorators import login_required,permission_required
from .models import Mudeeriath
from django.contrib.auth.models import Group,User #,Permission

@login_required(login_url='/')
@permission_required('hawala.delete_mudeeriath',login_url='/admin')
def mudeeriath_delete(request,id):   
    query_mud=Mudeeriath.objects.filter(id=int(id))
    #return HttpResponse(num_rows_user)
    if query_mud.count()>0:
        mudh_obj=query_mud[0]
        user_query=User.objects.filter(id=mudh_obj.user.id)
        if user_query.count()>0:
            obj_user=user_query[0]
            try:
                obj_user.delete()
                mudh_obj.delete()
                message="مدیریت حذف شد {} ".format(id)
                #log_detail_vars="id+"-"+mudh_obj.code+"-"+mudh_obj.mudeeriath_name+"-"+mudh_obj.mudeeriath_contact+"-"+mudh_obj.mudeeriath_email+"-"+mudh_obj.date_joined
             
                
                messages.success(request,message)
            
            except Exception as e:
                messages.error(request,"مدیریت حذف نشد {} ".format(id))      
        else:    #no user
            messages.error(request,"مدیریت  موجود نیست {} ".format(id))        
    else:
        messages.error(request,"مدیریت  موجود نیست {} ".format(id))        
    return redirect("mudeeriath_show")         
        
    

@login_required(login_url='/') 
@permission_required('hawala.add_mudeeriath',login_url='/admin')
def mudeeriath_form(request,update_id=None):
    template=loader.get_template('hawala/mudeeriath_registration_user.html')
    
    context={
        # "groups":Group.objects.all().exclude(name="controllers_sub_users")
        'groups':Group.objects.all()
    }
    
    if update_id is not None:
        #return HttpResponse(Mudeeriath.objects.get(id=update_id))
        context["mudeeriath"]=Mudeeriath.objects.get(id=update_id)
    return HttpResponse(template.render(context,request))
    
    
@login_required(login_url='/')
@permission_required('hawala.view_mudeeriath',login_url='/admin')
def mudeeriath_show(request): 
    template=loader.get_template('hawala/mudeeriath_user_show.html')
    mudeeriath_obj=Mudeeriath.objects.all()
    if request.user.is_superuser: 
        context={
            'mudeeriaths':mudeeriath_obj,
        }
    else: 
        context={ 
            'mudeeriaths':Mudeeriath.objects.filter(mudeeriath_name=request.user.username),
             #'controllers':Controller.objects.all(),
        }

    #return HttpResponse(request.user.has_perm('hawala.delete_mudeeriath'))
    return HttpResponse(template.render(context,request)) 

@login_required(login_url='/')
@permission_required('hawala.add_mudeeriath',login_url='/admin')
def mudeeriath_save(request,update_id=None):
    # print(request.POST)
    mudeeriath_name=request.POST.get("username",None) 
    password1=request.POST.get("password1",None)
    mudeeriath_code=request.POST.get("mudeeriath_code",None)
    mudeeriath_contact=request.POST.get("contact_no",None) 
    mudeeriath_email=request.POST.get("mudeeriath_email",None)
    group=request.POST.get("group",None)
    date_registration=datetime.strptime(datetime.now().strftime("%Y-%m-%d"),"%Y-%m-%d") 
    date_registration=date2jalali(date_registration)
    date_registration=datetime.strptime(date_registration.strftime("%Y-%m-%d"),"%Y-%m-%d")
    #date_registration_str=date2jalali(date_registration).strftime("%Y-%m-%d")
    
    ######################update#####################
    if update_id is not None:
        import urllib.parse
        mudeeriath_name=urllib.parse.unquote(str(mudeeriath_name)).replace('/','')
        query_mudh=Mudeeriath.objects.filter(id=int(update_id))
        # num_rows_user_update=len(obj_user)      
        # print("query_mudh ",query_mudh," obj_user ",obj_user," mudeeriath_name ",mudeeriath_name)
        # return HttpResponse(["query_mudh ",query_mudh," obj_user ",obj_user," mudeeriath_name ",mudeeriath_name]) 
        if query_mudh.count()==0:
            messages.error(request," مدیریت موجود نیست  {}  {}".format(mudeeriath_name,mudeeriath_code))
        else:
            obj_user=query_mudh[0].user
            #1 insert to mudeeriath
            if obj_user.count()<1:
                messages.error(request," مدیریت کاربر موجود نیست  {}  {}".format(mudeeriath_name,mudeeriath_code))
            #obj=Mudeeriath(mudeeriath_name=mudeeriath_name,mudeeriath_code=mudeeriath_code,mudeeriath_email=mudeeriath_email,mudeeriath_contact=mudeeriath_contact,date_joined=date_registration)
            try:
                #2 create_user

                group_obj=Group.objects.get(name=group)
                
                user=obj_user[0]
                user.username=mudeeriath_name 
                user.email=mudeeriath_email
                user.is_staff=True
                user.is_active=True
                user.date_joined=date_registration
                user.groups.add(group_obj)
                user.set_password(password1)
                user.save()
                
                print("obj_user ",model_to_dict(obj_user[0]))
                # obj_user[0].save()
                query_mudh.update(user=user,mudeeriath_name=mudeeriath_name,mudeeriath_code=mudeeriath_code,mudeeriath_email=mudeeriath_email,mudeeriath_contact=mudeeriath_contact,date_joined=date_registration,password=password1)         
                
                messages.success(request,"مدیریت تجدید شد  {}  {}".format(mudeeriath_name,mudeeriath_code))
                
            except Exception as e:
                messages.error(request,"مدیریت تجدید نشد {}    {}".format(mudeeriath_name,e))
        return redirect("mudeeriath_show")
    ########################end_update###############
    
    else: #new insert    
        num_rows_user=User.objects.filter(username=mudeeriath_name).count()
        num_rows_mudeeriath=Mudeeriath.objects.filter(mudeeriath_name=mudeeriath_name).count()
        #return HttpResponse(str(num_rows_user)+" "+str(num_rows_mudeeriath))
        if num_rows_user>0 or num_rows_mudeeriath>0:
            messages.error(request,"مدیریت موجود است {}  {}".format(mudeeriath_name,mudeeriath_code))      
        else:
            #1 insert to mudeeriath
            try:
                user_obj=User.objects.create_user(username=mudeeriath_name,password=password1,email=mudeeriath_email,is_active=True,is_staff=True,date_joined=date_registration)
                group_obj=Group.objects.get(name=group) 
                user_obj.groups.add(group_obj)
                mudeeriath=Mudeeriath(user=user_obj,mudeeriath_name=mudeeriath_name,mudeeriath_code=mudeeriath_code,mudeeriath_email=mudeeriath_email,mudeeriath_contact=mudeeriath_contact,date_joined=date_registration)
                mudeeriath.save()
                messages.success(request,"مدیریت ثبت شد  {}  {}".format(mudeeriath_name,mudeeriath_code))
                #2 create_user

            except Exception as e:
                user_obj.delete()
                messages.error(request,"اولا دیده شود که کدام یوزر به این نام مدیریت نباشد دوهم دیده شود که کدام مسءله تخنیکی نباشد. مدیریت ثبت نشد {}    {}".format(mudeeriath_name,e))
                
            
        return redirect("mudeeriath_show")
 
