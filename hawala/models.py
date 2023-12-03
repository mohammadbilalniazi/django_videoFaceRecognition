from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Mudeeriath(models.Model):
    mudeeriath_code=models.IntegerField(validators=[MaxValueValidator(10000),MinValueValidator(0)],unique=True)
    mudeeriath_name=models.CharField(max_length=40,unique=True)
    #mudeeriath_head=models.CharField(max_length=40,blank=True,null=True) 
    mudeeriath_contact=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    mudeeriath_email=models.CharField(max_length=40)
    date_joined=models.DateField()
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
      
    def __str__(self):
        return f"{self.mudeeriath_name}"
    
    class Meta:
        verbose_name_plural='مدیریت '
  
class Controller(models.Model):  
    # first_name = models.CharField(max_length=50,blank=False) 
    # last_name = models.CharField(max_length=50,blank=False)
    # email=models.EmailField() 
    user=models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
    # group=models.ForeignKey(Group,on_delete=models.SET_NULL,null=True,blank=False)
    father_name=models.CharField(max_length=50,blank=False)
    password=models.CharField(max_length=50,blank=False)
    skoonath_asli=models.CharField(max_length=80,blank=False)
    skoonath_filee=models.CharField(max_length=80,blank=False)
    wazeefa=models.CharField(max_length=50,blank=False)
    qadam=models.CharField(max_length=15)
    id_card=models.CharField(max_length=20,default="No")
    dob=models.DateField()
    pdo=models.CharField(max_length=20)
    basth=models.CharField(max_length=50,blank=False)
    mobile=models.CharField(max_length=15,blank=False)
    mobile_aqarib=models.CharField(max_length=15,blank=False)
    mudeeriath=models.ForeignKey(Mudeeriath,on_delete=models.DO_NOTHING,null=True,blank=False)
    class Meta:
        verbose_name_plural = "کنترولر"
        unique_together=('father_name','mudeeriath',)
