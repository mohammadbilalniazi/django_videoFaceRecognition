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
from django.core.files.base import ContentFile
from haziri.models import Daily_Haziri
from logs.models import Log
from profiles.models import Profile
from django.contrib.auth.models import User
from django.forms.models import model_to_dict


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
    if user_query.exists():
        user=user_query[0]
        profile=Profile.objects.get(user=user) 
        log=Log()
        log.photo=contentfile
        log.profile=profile

        daily_haziri=Daily_Haziri()
        daily_haziri.user=user
        try:
            daily_haziri.save()
            log.save()
            ok=True
            message="Thank You"
        except Exception as e:
            print("daily haziri ",e)
            ok=False
            message=str(e)
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