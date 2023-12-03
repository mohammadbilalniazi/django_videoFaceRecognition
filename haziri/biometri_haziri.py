from .models import Daily_Haziri
from django.template import loader
from django.http import HttpResponse

def daily_haziri_form(request):
    template=loader.get_template("haziri/daily_haziri.html")
    return HttpResponse(template.render({},request))
