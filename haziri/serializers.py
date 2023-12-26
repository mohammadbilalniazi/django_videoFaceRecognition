from rest_framework import serializers
from rest_framework import response

from jalali_date import datetime2jalali, date2jalali
import datetime
from .models import Haziri,Monthly_Haziri,Leave,General_Holidays
from hawala.models import Controller

class LeaveSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Leave
        fields=["id","user_id","accepted_by","start_date","reason","status"]

class GeneralHolidaysSerializer(serializers.ModelSerializer):
    class Meta:
        model=General_Holidays
        fields=["id","date","holiday","status"]
        
class Monthly_Haziri_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Monthly_Haziri
        # fields='__all__'
        
        fields=["id","user_id","total_present","kaifyath_haziri","total_absent","total_leave","status","total_tafrihi","total_zaroori","total_marizi","total_waladi","total_hajj"]

class Haziri_Serializer(serializers.ModelSerializer):
    monthly_haziri_set = Monthly_Haziri_Serializer(many=True)
    class Meta:
        model=Haziri
        fields=["id","monthly_haziri_set","mudeeriath","month","report_date","status","created_by"] #month===> kaifyath_haziri

    def create(self, validated_data):
        haziri_report_set = validated_data.pop('monthly_haziri_set')
        print("###########validated_data ",validated_data)
        haziri = Haziri.objects.create(**validated_data)
        haziri.save()
        for haziri_report in haziri_report_set:
            h = Monthly_Haziri.objects.create(haziri=haziri, **haziri_report)
            h.save()
        return haziri





class ControllerHaziriSerializer(serializers.ModelSerializer):
    kaifyath_haziri = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    month=serializers.SerializerMethodField()
    user_name=serializers.SerializerMethodField()
    mudeeriath_id=serializers.SerializerMethodField()
    is_haziri_uploaded=serializers.SerializerMethodField()
    report_date=serializers.SerializerMethodField()
    total_present=serializers.SerializerMethodField()
    total_absent=serializers.SerializerMethodField()
    total_leave=serializers.SerializerMethodField()

    total_tafrihi=serializers.SerializerMethodField()
    total_zaroori=serializers.SerializerMethodField()
    total_marizi=serializers.SerializerMethodField()
    total_waladi=serializers.SerializerMethodField()
    total_hajj=serializers.SerializerMethodField()

    haziri_status=serializers.SerializerMethodField()
    monthly_haziri_status=serializers.SerializerMethodField()
    mudeeriath_name=serializers.SerializerMethodField()
    first_name=serializers.SerializerMethodField()
    class Meta:
        model=Controller
        fields=['id','first_name','father_name','user_id','user_name','qadam','basth','mudeeriath_id','mudeeriath_name','wazeefa','is_haziri_uploaded','kaifyath_haziri','report_date','monthly_haziri_status','haziri_status','total_present','total_absent','total_leave','month',"total_tafrihi","total_zaroori","total_marizi","total_waladi","total_hajj"]
    
    def get_user_id(self,obj):
        # self.user_name=obj.first_name+"_"+obj.last_name
        
        self.user_name=obj.user.username
        # print("self.user_name ",self.username)
        # return HttpResponse("test")
        self.start_date=self.context.get("start_date")
        # self.end_date=self.context.get("end_date")
        self.start_date=datetime.datetime.strptime(str(self.start_date),"%Y-%m-%d")
        # self.end_date=datetime.datetime.strptime(str(self.end_date),"%Y-%m-%d")
        try:
            self.user_obj=obj.user
            #print("###############################self.user_name=################################",self.user_obj.id)
            return obj.user.id
        except Exception as e:
            return e
    def get_first_name(self,obj):
        return obj.user.first_name
    def get_user_name(self,obj):
        #user_name=obj.first_name+"_"+obj.last_name  
        #print("###############################self.user_name=################################",self.user_name)
        return self.user_name

    def get_mudeeriath_id(self,obj):
        # print("###############################self.mudeeriath=################################",obj.mudeeriath.id)
        return obj.mudeeriath.id
        
    def get_mudeeriath_name(self,obj):
        # print("###############################self.mudeeriath=################################",obj.mudeeriath.id)
        return obj.mudeeriath.mudeeriath_name
    
    def get_is_haziri_uploaded(self,obj):
        # self.user_name=obj.first_name+"_"+obj.last_name
        # self.user_obj=User.objects.filter(username=self.user_name)
        self.date=datetime.datetime.now().strftime('%Y-%m-%d')
        self.date=datetime.datetime.strptime(self.date,"%Y-%m-%d")
        self.date=date2jalali(self.date)
        self.month=str(self.start_date).split("-")[1]
        self.year=str(self.start_date).split("-")[0]
        self.haziri_query=Haziri.objects.filter(month=int(self.month),fiscalyear=int(self.year),monthly_haziri__user_id=self.user_obj)
        #self.haziri_query=Haziri.objects.filter(start_date__lte=self.start_date,end_date__gte=self.end_date) # 1401-01-01     1401-01-09
        if self.haziri_query.count()>0:
            self.haziri_obj=self.haziri_query[0]
            self.kaifyath_haziri=self.haziri_obj.monthly_haziri_set.all()[0].kaifyath_haziri
            self.status=self.haziri_obj.status 
            return True
        else:
            self.kaifyath_haziri=""
            self.status=1 
            return False
    
    def get_monthly_haziri_status(self,obj):
        # print("#####################self.start###################",self.start_date,"###############end_date############",self.end_date)
        # self.monthly_haziri_query=Monthly_Haziri.objects.filter(user_id=self.user_obj.id,haziri__start_date__gte=self.start_date,haziri__end_date__lte=self.end_date)
        self.monthly_haziri_query=Monthly_Haziri.objects.filter(user_id=self.user_obj.id,haziri__month=int(self.month),haziri__fiscalyear=int(self.year))
        if self.monthly_haziri_query.count()>0:
            self.monthly_haziri_obj=self.monthly_haziri_query[0]
            self.total_present=self.monthly_haziri_obj.total_present
            self.total_absent=self.monthly_haziri_obj.total_absent
            self.total_leave=self.monthly_haziri_obj.total_leave 
            self.status=self.monthly_haziri_obj.status
            
            
            self.total_tafrihi=self.monthly_haziri_obj.total_tafrihi
            self.total_zaroori=self.monthly_haziri_obj.total_zaroori
            self.total_marizi=self.monthly_haziri_obj.total_marizi
            self.total_waladi=self.monthly_haziri_obj.total_waladi 
            self.total_hajj=self.monthly_haziri_obj.total_hajj
            
        else:
            self.total_present=0
            self.total_absent=0
            self.total_leave=0
            self.total_tafrihi=0
            self.total_zaroori=0
            self.total_marizi=0
            self.total_waladi=0
            self.total_hajj=0
            self.status=1
        # print("#################################self.total_present#################################=",self.total_present)
        return self.status

    def get_haziri_status(self,obj):     
        return self.status
    
    def get_kaifyath_haziri(self,obj):
        return self.kaifyath_haziri
    
    def get_month(self,obj):
        return self.month
    
    def get_report_date(self,obj):
        self.date=self.date.strftime("%Y-%m-%d")
        # print("serializer controller date=",self.date)
        return self.date
    
    def get_total_leave(self,obj):
        return self.total_leave
    
    def get_total_absent(self,obj):
        return self.total_absent
    
    def get_total_present(self,obj):
        return self.total_present

    def get_total_tafrihi(self,obj):
        return self.total_tafrihi
    
    def get_total_zaroori(self,obj):
        return self.total_zaroori
    
    def get_total_marizi(self,obj):
        return self.total_marizi

    def get_total_waladi(self,obj):
        return self.total_waladi
    
    def get_total_hajj(self,obj):
        return self.total_hajj
    
 
