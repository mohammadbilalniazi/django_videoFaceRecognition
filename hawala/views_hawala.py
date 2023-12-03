from .models import Mudeeriath,Controller
def get_mudeeriath(request,controller_id=None,mudeeriath_id=None):

    if mudeeriath_id!=None:
        if mudeeriath_id=="all": ####################mudeeriath maybe id or name i will check
            query_mudh=Mudeeriath.objects.all().order_by('-pk')
        else:
            query_mudh=Mudeeriath.objects.filter(id=int(mudeeriath_id))
    elif controller_id!=None:
        query_mudh=Mudeeriath.objects.filter(controller__id=int(controller_id))

    else:
        if request.user.is_superuser: 
            query_mudh=Mudeeriath.objects.all() 
        elif Mudeeriath.objects.filter(user=request.user).exists():    
            query_mudh=Mudeeriath.objects.filter(mudeeriath_name=request.user.username)
            
        elif Controller.objects.only('mudeeriath').filter(user=request.user).exists(): #and User.objects.filter(groups__name="sub_user").exists():
            cont_obj=Controller.objects.get(user=request.user)
            query_mudh=Mudeeriath.objects.filter(id=int(cont_obj.mudeeriath.id))
    return query_mudh
