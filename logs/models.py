from django.db import models
from profiles.models import Profile
from datetime import datetime
from hawala.date_changing import current_shamsi_date 
from haziri.models import Daily_Haziri
# Create your models here.
from django.forms.models import model_to_dict

current_date=current_shamsi_date()

def image_path(self,filename):
    import time
    import pathlib
    import os
    from django.conf import settings
    current_time=time.strftime("%H_%M_%S", time.localtime())
    image_name=current_time+".png"
    # path=os.path.join(current.split("-")[0]+"/"+current.split("-")[1]+"/"+current.split("-")[2]+"/"+image_name)
    # path=pathlib.PurePath(settings.MEDIA_ROOT,pathlib.Path(image_path_name))
    folder="logs"+"/"+current_date.split("-")[0]+"/"+current_date.split("-")[1]+"/"+current_date.split("-")[2]
    folder_path=pathlib.PurePath(settings.MEDIA_ROOT,pathlib.Path(folder))
    try:
        os.makedirs(folder_path,exist_ok=False)
    except FileExistsError:
        print("FileExistsError")
        
    path=folder+"/"+image_name
    
    print("pure path ",str(path),'self ',model_to_dict(self),'filename ',filename)
    return path

class FaceLog(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    daily_haziri=models.ForeignKey(Daily_Haziri,on_delete=models.CASCADE,blank=True,null=True)
    # photo=models.ImageField(upload_to='logs')
    photo=models.ImageField(upload_to=image_path)  
    is_correct=models.BooleanField(default=False)
    date=models.DateField(default=datetime.strptime(current_date,"%Y-%m-%d"))
    year=models.SmallIntegerField(default=current_date.split('-')[0])
    month=models.SmallIntegerField(default=current_date.split('-')[1])
    day=models.SmallIntegerField(default=current_date.split('-')[2])
    created=models.TimeField(auto_now=True)

    def __str__(self):
        if hasattr(self,'profile'):
            try:
                return f"Log of profile {self.profile.id}"
            except:
                return "No Profile"
        else:
            return "No Profile"

