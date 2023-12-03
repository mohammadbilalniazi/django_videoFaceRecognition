
from django import forms
from .models import Controller
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

class ControllerForm(forms.ModelForm):
    class Meta:
        model=Controller
        fields="__all__"
        
    def __init__(self,*args,**kwargs):
        super(ControllerForm,self).__init__(*args,**kwargs)
        self.fields["dob"]=JalaliDateField(label=("تاریخ حواله"),widget=AdminJalaliDateWidget)#,months=MONTH_CHOICES
        self.fields["dob"].widget.attrs['tabindex']="9"
        # self.fields['date_hawala'].widget.attrs.update({'class': 'jalali_date-date'})
