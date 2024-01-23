
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from .forms import ControllerForm
from django.contrib import messages
from jalali_date import  date2jalali
from django.contrib.auth.decorators import login_required,permission_required
from .models import Controller,Mudeeriath
from django.contrib.auth.models import Group,User
from profiles.models import Profile
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse
from .views_hawala import get_mudeeriath
from common.file_management import delete_file
@login_required(login_url='/')
@permission_required('hawala.view_controller',login_url='')
def controller_show(request,mudeeriath=None):
    template=loader.get_template('hawala/controller_show.html')
    # user = get_object_or_404(User, pk=request.user.id)       #admin defa
    #return HttpResponse(Controller.objects.filter(mudeeriath=user))
    if request.user.is_superuser:
        context={'controllers':Controller.objects.all()}
    else:  
        if Mudeeriath.objects.filter(mudeeriath_name=request.user.username).exists():
            obj_mudh=Mudeeriath.objects.get(mudeeriath_name=request.user.username)
            print("Mudeeriath")
        elif Controller.objects.filter(user=request.user).exists() and request.user.groups.filter(name="controllers_sub_users").exists():
            obj_cont=Controller.objects.get(user=request.user)
            mudeeriath_name=obj_cont.mudeeriath
            obj_mudh=Mudeeriath.objects.get(mudeeriath_name=mudeeriath_name)
        context={ 
                'controllers':obj_mudh.controller_set.all()
            }
    #return HttpResponse(request.user.has_perm('hawala.delete_controller'))
    return HttpResponse(template.render(context,request)) 
 
@api_view(('GET',))
def controllers_mudeeriath(request,mudeeriath="all"):
    #return HttpResponse(mudeeriath_id)
    if mudeeriath=="all": ####################mudeeriath maybe id or name i will check
        query_set=Controller.objects.all().order_by('-pk')
    else:
        mudeeriath_obj=Mudeeriath.objects.filter(mudeeriath_name=str(mudeeriath))  
        query_set=Controller.objects.filter(mudeeriath=mudeeriath_obj[0]).values_list("first_name")   

    context={}
    context['controllers']=list(query_set,flat=True)
    #data={'shamsi':str(date_shamsi),'miladi':str(date_miladi),'qamari':str(date_qamari)}
    print(context)
    return JsonResponse(json.dumps(context), safe=False)#serialized 

@login_required(login_url='/')
@permission_required('hawala.add_controller',login_url='/admin/')
def controller_form(request,id=None):
    template=loader.get_template('hawala/controller_form.html')
    if request.user.is_superuser:
        context={
            'groups':Group.objects.all().exclude(name="controller_user"), 
            'mudeeriaths':Mudeeriath.objects.all()
        }
    else: 
        context={
            'groups':Group.objects.filter(name="controllers_sub_users"), 
            'mudeeriaths':get_mudeeriath(request)
        }
        #print(context)
    form=ControllerForm() 
    context['form']=form
    if id!=None:
        if Controller.objects.filter(id=int(id)).count()>0:
            controller_obj=Controller.objects.get(id=int(id))
            context['controller_obj']=controller_obj
            context['update_id']=int(id)
            context['mud_of_cont_to_be_update']=controller_obj.mudeeriath
    
    return HttpResponse(template.render(context,request)) 



@login_required(login_url='/')
@permission_required('hawala.add_controller',login_url='/admin/')
@permission_required('hawala.change_controller',login_url='/admin/')
def controller_save(request):  
    print("request.POST",request.POST)
    print("file ",request.FILES)
    # return HttpResponse("test")

    update_id=request.POST.get("update_id")
    if "photo" in request.FILES:
        photo=request.FILES['photo']
    else:
        photo=None
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name') 
    father_name=request.POST.get('father_name')
    id_card=request.POST.get('id_card')
    skoonath_asli=request.POST.get('skoonath_asli')
    skoonath_filee=request.POST.get('skoonath_filee')
    wazeefa=request.POST.get('wazeefa')
    basth=request.POST.get('basth')
    mobile=request.POST.get('mobile')
    pdo=request.POST.get('pdo',None)
    dob=request.POST.get('dob',None)
    mobile_aqarib=request.POST.get('mobile_aqarib')
    mudeeriath=request.POST.get('mudeeriath')
    # username=request.POST.get("username")
    qadam=request.POST.get('qadam',1)
    password=request.POST.get('password')
    try:
        mudeeriath=Mudeeriath.objects.get(mudeeriath_name=mudeeriath)
    except:
        return HttpResponseRedirect(reverse("controller_form"))
    email=request.POST.get('email')
    group=request.POST.get('group') 
    group_obj=Group.objects.get(name=group)
    
    if update_id!=None and update_id!="":
        obj_cont=Controller.objects.get(id=int(update_id))

        user=obj_cont.user
        user.username=email
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.groups.clear()
        user.groups.add(group_obj)
        user.set_password(password)
        obj_cont.father_name=father_name
        obj_cont.id_card=id_card
        obj_cont.pdo=pdo
        obj_cont.skoonath_asli=skoonath_asli
        obj_cont.skoonath_filee=skoonath_filee
        obj_cont.wazeefa=wazeefa
        obj_cont.mudeeriath=mudeeriath
        obj_cont.qadam=qadam
        obj_cont.mobile_aqarib=mobile_aqarib
        obj_cont.mobile=mobile
        obj_cont.password=password
            
        profile=Profile.objects.get(user=user)
        
        (ok,message)=delete_file(profile,"photo")
        print("ok ",ok," message ",message)
        # return HttpResponse("update")    
    else: # new user
        
        query_user=User.objects.filter(email=email)
        query_controller=Controller.objects.filter(id_card=id_card)
        if query_controller.count()>0:
            messages.error(request,"کنترولر {} موجود است".format(first_name))
            messages.error(request,'کنترولر {} به سیستم داخل نشد '.format(first_name)) 
            return redirect("/controller/update/"+str(query_controller[0].id)) 
        elif query_user.count()>0:
            messages.error(request,"یوزر {} موجود است".format(first_name))
            messages.error(request,'یوزر {} به سیستم داخل نشد '.format(first_name))
            return HttpResponseRedirect(reverse("controller_form")) 

        obj_cont=Controller(father_name=father_name,id_card=id_card,pdo=pdo,dob=dob,skoonath_asli=skoonath_asli,skoonath_filee=skoonath_filee,wazeefa=wazeefa,basth=basth,mobile=mobile,mobile_aqarib=mobile_aqarib,mudeeriath=mudeeriath,qadam=qadam,password=password)
        # return HttpResponse("not update")
    
        if request.user.is_superuser:
            user = User.objects.create_user(username=email,first_name=first_name,last_name=last_name,email=email,password=password,is_staff=True,is_active=True) 
            # message="یوز {}  ".format(username,password)
        else:
            user = User.objects.create_user(username=email,first_name=first_name,last_name=last_name,email=email,password=password,is_staff=True,is_active=False) 
            messages.success(request,"  اجازه ورود را از ادمین بگیرید ")
    try:   
        user.groups.add(group_obj)
        obj_cont.user=user
        user.save()
        obj_cont.save()
        profile_query=Profile.objects.filter(user=user)
        if profile_query.count()>0:
            profile=profile_query[0]
        else:
            profile=Profile() 
        profile.photo=photo
        profile.bio="nothing"
        profile.save()
        messages.success(request,'یوزر {}'.format(email))
        messages.success(request,'پاسورد {}   '.format(password))
    except Exception as e:
        if update_id==None and update_id=="":
            user.delete()
        messages.error(request,'کنترولر {} به سیستم داخل نشد '.format(first_name))
        messages.error(request,' {} '.format(e))
    return redirect("/controller/update/"+str(obj_cont.id))
            
            
        

@login_required(login_url='/')
@permission_required('hawala.delete_controller')
def controller_delete(request,id):  
    #print(int(id))
    #return HttpResponse(type(id))
    row_obj=Controller.objects.filter(id=int(id))#=1
    
    #return HttpResponse(row_obj)
    num_rows=len(row_obj)
    #return HttpResponse(num_rows)
    if num_rows==0:   # the hawal is there to be approved by thadyath
        messages.error(request,'کنترولر موجود نیست {}'.format(id))
        return HttpResponseRedirect(reverse("controller_show"))
    else: 
        cont_obj=Controller.objects.get(id=int(id))
        #print(dir(cont_obj))
        username=cont_obj.first_name+'_'+cont_obj.last_name
        user_obj=User.objects.get(username=cont_obj.email)
        try:  
            user_obj.delete()
            cont_obj.delete()
        except Exception as e:
            user_obj.delete()
            
        messages.success(request,'کنترولر حذف شد {}'.format(id))
        return HttpResponseRedirect(reverse("controller_show"))
        


