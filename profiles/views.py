from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from django_video2.face import classify_face
import base64
from datetime import datetime
from django.core.files.base import ContentFile
from haziri.models import Daily_Haziri,HowManyTimeHaziri
from logs.models import Log
from profiles.models import Profile
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from hawala.date_changing import current_shamsi_date 

def login_view(request):
    return render(request,'login.html',{})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    return render(request,'main.html',{})

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def find_user_view(request):
    # if able to find user
    # print("request.data ",request.data.keys())
    photo=request.data['photo']
    # print(photo)
    _,str_img=photo.split(";base64")
    decoded_file=base64.b64decode(str_img) # base64 file
    # print("decoded_file ",decoded_file)
    contentfile=ContentFile(decoded_file,'upload.png')
    
    # res=classify_face(log.photo.path)
    res=classify_face(contentfile) 
    print("res=",res)
    user_query=User.objects.filter(username=res)
    # print("contentfile ",contentfile) #outputs raw content
    print("user_query.exists() ",user_query.exists())
    howmanytimehaziries=HowManyTimeHaziri.objects.all()
    if len(howmanytimehaziries)>0:
        times=howmanytimehaziries[0].times
    else:
        times=1
    
    if user_query.exists():
        user=user_query[0]
        profile=Profile.objects.get(user=user) 
        # log=Log()
        current=current_shamsi_date()


        daily_haziris=Daily_Haziri.objects.filter(user=user,date=datetime.strptime(current,"%Y-%m-%d"))

        logs=Log.objects.filter(profile=profile,date=datetime.strptime(current,"%Y-%m-%d"))
        daily_haziri=Daily_Haziri()
        if len(logs)<times:
            log=Log()
            log.photo=contentfile
            log.profile=profile
            
            daily_haziri.user=user
            message="Thank You"
            ok=True
            try:
                daily_haziri.save()
                # ok=True
                # message="Thank You"
            except Exception as e:
                print("daily haziri ",e)
                if daily_haziris.count()>0:
                    daily_haziri=daily_haziris[0]
            log.daily_haziri=daily_haziri
            log.save()
        else:
            ok=False
            message="You Have Already Have 2 Times Attendance Today "
        data=model_to_dict(user)
        if 'groups' in data:
            del data['groups']
      
        print("data {} ok {} message {} ".format(data,ok,message))
        # login(request,user)
    else:
        data={}
        message='Not Authenticated'
        ok=False
    return Response({'ok':ok,"data":data,"message":message})