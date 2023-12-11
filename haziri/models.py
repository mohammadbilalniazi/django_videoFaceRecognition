from django.db import models
from django.contrib.auth.models import User
from hawala.models import Mudeeriath
# Create your models here.
from datetime import datetime
from hawala.date_changing import current_shamsi_date 
HAZIRI_CHOICES=((0,"Close"),(1,"Open"),(2,"Suspended"))# 0 close 1 open 2 suspended
HOLIDAYS_CHOICES=((0,"Close"),(1,"Open"))# 0 close 1 open 2 
LEAVE_CHOICES=((0,0),(1,1),(2,2))# 0 rejected 1 accepted 2 pending 
MONTHS=((1,"حمل"),(2,"ثور"),(3,"جوزا"),(4,"سرطان"),(5,"اسد"),(6,"سنبله"),(7,"میزان"),(8,"عقرب"),(9,"قوس"),(10,"جدی"),(11,"دلو"),(12,"حوت"))
class Haziri(models.Model):    
    mudeeriath=models.ForeignKey(Mudeeriath,on_delete=models.DO_NOTHING)
    month=models.SmallIntegerField(choices=MONTHS)
    fiscalyear=models.SmallIntegerField(default=int(current_shamsi_date().split("-")[0]),null=True)
    report_date=models.DateField()
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.SmallIntegerField(choices=HAZIRI_CHOICES,default=1)
    created_by=models.CharField(max_length=22)
    class Meta:
        unique_together=("mudeeriath","month","fiscalyear")

class Daily_Haziri(models.Model): 
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)   
    date=models.DateField(default=datetime.strptime(current_shamsi_date(),"%Y-%m-%d"))
    is_active=models.BooleanField(default=False)
    class Meta:
        unique_together=("user","date")
class Monthly_Haziri(models.Model): 
    haziri=models.ForeignKey(Haziri,models.CASCADE)
    kaifyath_haziri=models.TextField(null=True,blank=True)
    user_id=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    total_present=models.SmallIntegerField()
    total_absent=models.SmallIntegerField(default=0)
    total_leave=models.SmallIntegerField(default=0)
    total_tafrihi=models.SmallIntegerField(default=0)
    total_zaroori=models.SmallIntegerField(default=0)
    total_marizi=models.SmallIntegerField(default=0)
    total_waladi=models.SmallIntegerField(default=0)
    total_hajj=models.SmallIntegerField(default=0)
    status=models.SmallIntegerField(choices=HAZIRI_CHOICES,default=1)
    class Meta:
        verbose_name_plural="تفصیل حاضری"
    #unique_together=("date","holiday")
    

class Leave(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    accepted_by=models.CharField(max_length=25)
    start_date=models.DateField()
    end_date=models.DateField()
    reason=models.TextField(blank=True,null=True)
    status=models.SmallIntegerField(choices=LEAVE_CHOICES)

    class Meta:
        verbose_name_plural="رخصتی درخواستی"
        unique_together=("start_date","user_id")



class General_Holidays(models.Model):
    date=models.DateField()
    holiday=models.CharField(max_length=40)
    status=models.BooleanField(choices=HOLIDAYS_CHOICES)

    class Meta:
        verbose_name_plural="روزهای روخصتی"
        unique_together=("date","holiday")

    def __str__(self):
        return self.holiday
