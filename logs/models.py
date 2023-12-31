from django.db import models
from profiles.models import Profile
from datetime import datetime
from hawala.date_changing import current_shamsi_date 
from haziri.models import Daily_Haziri
# Create your models here.
current_date=current_shamsi_date()
class FaceLog(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    daily_haziri=models.ForeignKey(Daily_Haziri,on_delete=models.CASCADE,blank=True,null=True)
    photo=models.ImageField(upload_to='logs') 
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

