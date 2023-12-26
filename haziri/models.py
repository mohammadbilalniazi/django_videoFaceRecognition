from django.db import models
from django.contrib.auth.models import User
from hawala.models import Mudeeriath
# Create your models here.
from django.dispatch import receiver
from django.db.models.signals import pre_save
from datetime import datetime
from hawala.date_changing import current_shamsi_date 
HAZIRI_CHOICES=((0,"Close"),(1,"Open"),(2,"Suspended"))# 0 close 1 open 2 suspended
TIMES_CHOICES=((1,"ONE"),(2,"TWO"),(3,"THREE"),(4,"FOUR"),(5,"FIVE"))
HOLIDAYS_CHOICES=((0,"Close"),(1,"Open"))# 0 close 1 open 2 
PER_CHOICES=((1,"Per Day"),(2,"Per Week"),(3,"Per Month"))# 0 close 1 open 2 

MONTHS=((1,"حمل"),(2,"ثور"),(3,"جوزا"),(4,"سرطان"),(5,"اسد"),(6,"سنبله"),(7,"میزان"),(8,"عقرب"),(9,"قوس"),(10,"جدی"),(11,"دلو"),(12,"حوت"))
class Haziri(models.Model):    
    mudeeriath=models.ForeignKey(Mudeeriath,on_delete=models.DO_NOTHING)
    month=models.SmallIntegerField(choices=MONTHS)
    fiscalyear=models.SmallIntegerField(default=int(current_shamsi_date().split("-")[0]),null=True)
    report_date=models.DateField()
    # start_date=models.DateField()
    # end_date=models.DateField()
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
    def __str__(self):
        return self.user.username
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

class HowManyTimeHaziri(models.Model):
    name=models.CharField(max_length=25,null=True)
    times=models.SmallIntegerField(choices=TIMES_CHOICES,default=1)
    per=models.SmallIntegerField(choices=PER_CHOICES,default=1)
    is_active=models.BooleanField(default=True)

class ValidTimeHaziri(models.Model):
    name=models.CharField(max_length=25,null=True)
    fromTime=models.TimeField(auto_now=True)
    toTime=models.TimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


LEAVE_CHOICES=((0,0),(1,1),(2,2))# 0 rejected 1 accepted 2 pending 

class LeaveType(models.Model):
    name=models.CharField(max_length=25,null=True)
    duration=models.SmallIntegerField(default=0)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name+" "+str(self.duration)

class Leave(models.Model):
    leavetype=models.ForeignKey(LeaveType,on_delete=models.DO_NOTHING,default=1)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    accepted_by=models.CharField(max_length=30)
    month=models.SmallIntegerField(choices=MONTHS,default=int(current_shamsi_date().split("-")[1]))
    year=models.SmallIntegerField(default=int(current_shamsi_date().split("-")[0]),null=True)
    fromDay=models.SmallIntegerField(default=1)
    toDay=models.SmallIntegerField(default=1)
    reason=models.TextField(blank=True,null=True)
    status=models.SmallIntegerField(choices=LEAVE_CHOICES)

    class Meta:
        verbose_name_plural="رخصتی درخواستی"
        unique_together=("user","year","month","fromDay")

    def __str__(self):
        return str(self.leavetype)+'-'+str(self.user)

@receiver(pre_save,sender=Leave)
def validate_limitation(sender, instance, **kwargs):
    # if created or not created: # not created updated
    fd=instance.fromDay
    td=instance.toDay
    total=td-fd+1
    #in one Year it should not exceed the total of leave time limit with specific leavetype
    leaves=Leave.objects.filter(user=instance.user,year=instance.year)
    for leave in leaves.filter(leavetype=instance.leavetype):
        fd=leave.fromDay
        td=leave.toDay
        temp_total=(td-fd)+1
        total=total+temp_total
    if instance.pk is not None: # if not updated
        previous_leave=Leave.objects.get(id=instance.id)
        total_previous=previous_leave.fromDay-previous_leave.toDay+1
        total=total-total_previous
        print("instance.pk ",instance.pk," total_previous ",total_previous)
    #in one month overlapping
    overlap=leaves.filter(month=instance.month,fromDay__lte=instance.fromDay,toDay__gte=instance.toDay).exists()
    print("total leave=",total," limit ",instance.leavetype.duration," overlap ",overlap)
    if total>instance.leavetype.duration:
        raise ValueError("total leave is more than limit ")
        # return False
    elif total>instance.leavetype.duration or overlap:
        raise ValueError("Not Valid Period It is Overlapping")
        # return False
    return True


class General_Holidays(models.Model):
    date=models.DateField()
    holiday=models.CharField(max_length=40)
    status=models.BooleanField(choices=HOLIDAYS_CHOICES)

    class Meta:
        verbose_name_plural="روزهای روخصتی"
        unique_together=("date","holiday")

    def __str__(self):
        return self.holiday
