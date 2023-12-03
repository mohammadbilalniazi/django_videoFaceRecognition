from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User,Group
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class Languages(models.Model):
    language=models.CharField(max_length=30,unique=True)
    description=models.TextField()

    class Meta:
        # verbose_name =("")
        verbose_name_plural =("Languages")

    def __str__(self):
        return self.language
    

class Language_Detail(models.Model):
    language=models.ForeignKey(Languages,on_delete=models.DO_NOTHING,null=True)
    key=models.CharField(max_length=100)
    value=models.TextField(null=True)
    page=models.CharField(max_length=30,null=True,blank=True)

    class Meta:
        unique_together=(("language","key"))
        verbose_name_plural =("ترجمه")

class Assign_Languages(models.Model):
    languages=models.ForeignKey(Languages,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    class Meta:
        # verbose_name =("")
        verbose_name_plural =("User Language")
        unique_together=(("languages","user"))

    # def __str__(self):
    #     return self.name




class NawaSanad(models.Model):
    nawa_sanad=models.CharField(max_length=15,unique=True)
    nawa_sanad_code=models.IntegerField(unique=True,validators=[MaxValueValidator(1000),MinValueValidator(0)])
    description=models.CharField(null=True,unique=True,max_length=15,blank=True)
    class Meta:
        verbose_name_plural="نوع سند"

    def __str__(self):
        return f"{self.nawa_sanad}"



class Currency(models.Model):  
    applicationid=models.CharField(max_length=40,null=True)
    description=models.CharField(max_length=40,null=True)
    name=models.CharField(max_length=40,unique=True)
    is_active=models.BooleanField(default=True)
    
    is_domestic=models.BooleanField(null=True)
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural='پولی واحد'

class Location(models.Model):  
    location_code=models.IntegerField(validators=[MaxValueValidator(10000),MinValueValidator(0)],unique=True)
    location_name=models.CharField(max_length=40,unique=True)
    #mudeeriath_head=models.CharField(max_length=40,blank=True,null=True) 
    location_contact=models.CharField(max_length=40)
    location_email=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.location_name}"
    
    class Meta:
        verbose_name_plural='موقعیت'