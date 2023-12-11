from django import forms
import pytz
from .models import Haziri,Monthly_Haziri,Leave
from datetime import datetime
from jalali_date import date2jalali
from jalali_date.widgets import AdminJalaliDateWidget
from jalali_date.fields import JalaliDateField


class HaziriForm(forms.Form):
    class Meta:
        fields="__all__"      
        model=Haziri
    def __init__(self,*args, **kwargs):
        super(HaziriForm,self).__init__(*args,**kwargs)
        
        date=pytz.timezone("Asia/Kabul").localize(datetime.now()).strftime('%Y-%m-%d')
        date=datetime.strptime(date,'%Y-%m-%d')
        date_hijri=date2jalali(date)
        end_date_initial_value=date_hijri
        year=date_hijri.strftime("%Y")
        month=date_hijri.strftime("%m")
        start_date_initial_value=year+"-"+month+"-01"
        print("#############################################")
        print("start_date_initial_value=",start_date_initial_value)
        #start_date_initial_value=datetime.strptime(start_date_initial_value,"%Y-%m-%d")

        
        self.fields["start_date"]=JalaliDateField(label="شروع",widget=AdminJalaliDateWidget)
        self.fields["start_date"].widget.attrs['tabindex']="1"
        self.fields["start_date"].widget.attrs['id']='start_date_input'
        self.fields["start_date"].widget.attrs['name']='start_date_input'
        self.fields["start_date"].widget.attrs['onchange']='controllers_haziri()'
        self.fields["start_date"].initial=start_date_initial_value

        self.fields["end_date"]=JalaliDateField(label="ختم",widget=AdminJalaliDateWidget)
        self.fields["end_date"].widget.attrs['tabindex']="2"
        self.fields["end_date"].widget.attrs['id']="end_date_input"
        self.fields["end_date"].widget.attrs['name']="end_date_input"
        self.fields["end_date"].widget.attrs['onchange']='controllers_haziri()'
        self.fields["end_date"].initial=end_date_initial_value
        
        self.fields["date"]=JalaliDateField(label="شروع",widget=AdminJalaliDateWidget)
        self.fields["date"].widget.attrs['tabindex']="1"
        self.fields["date"].widget.attrs['id']='start_date_input'
        self.fields["date"].initial=date_hijri
       
 

 
class Leave_Form(forms.Form):
    class Meta:
        fields="__all__"
        model=Leave        
    def __init__(self,*args, **kwargs):
        super(Leave_Form,self).__init__(*args,**kwargs)
        date=pytz.timezone("Asia/Kabul").localize(datetime.now()).strftime('%Y-%m-%d')
        date=datetime.strptime(date,'%Y-%m-%d')
        date_hijri=date2jalali(date)
        #start_date_initial_value=datetime.strptime(start_date_initial_value,"%Y-%m-%d")  
        self.fields["start_date"]=JalaliDateField(label="شروع",widget=AdminJalaliDateWidget)
        self.fields["start_date"].widget.attrs['tabindex']="1"
        self.fields["start_date"].widget.attrs['id']='start_date_input'
        self.fields["start_date"].initial=date_hijri

        self.fields["end_date"]=JalaliDateField(label="ختم",widget=AdminJalaliDateWidget)
        self.fields["end_date"].widget.attrs['tabindex']="2"
        self.fields["end_date"].widget.attrs['id']="end_date_input"
        self.fields["end_date"].initial=date_hijri
 