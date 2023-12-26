"""
URL configuration for django_video2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import (login_view,logout_view,home_view,find_user_view)
from haziri import views_haziri
from hawala import views_controller,views_mudeeriath

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home_view,name='home'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('classify/',find_user_view,name='classify'),   

    path('controller/delete/<str:id>',views_controller.controller_delete,name='controller_delete'),
    path('admin/hawala/controller/',views_controller.controller_show,name='controller_show'),
    path('controller/update/<id>',views_controller.controller_form,name="update_controller_form"),
    path('controllers_mudeeriath/<mudeeriath>/',views_controller.controllers_mudeeriath,name='controllers_mudeeriath'),
    path('admin/hawala/controller/save/',views_controller.controller_save),
    path('admin/hawala/controller/add/',views_controller.controller_form,name="controller_form"),

    path('admin/haziri/haziri/',views_haziri.haziri_form),
    path('admin/haziri/haziri/add/',views_haziri.haziri_form),
    path('admin/haziri/monthly_haziri/',views_haziri.haziri_form),
    path('admin/haziri/monthly_haziri/add/',views_haziri.haziri_form),
    path('haziri/',include('haziri.urls')),

    path('mudeeriath/delete/<str:id>',views_mudeeriath.mudeeriath_delete,name='mudeeriath_delete'),
    path('admin/hawala/mudeeriath/',views_mudeeriath.mudeeriath_show,name='mudeeriath_show'),
    path('admin/hawala/mudeeriath/add/',views_mudeeriath.mudeeriath_form,name='mudeeriath_form'),
    path('mudeeriath/save/<str:update_id>',views_mudeeriath.mudeeriath_save), 
    path('mudeeriath/save/',views_mudeeriath.mudeeriath_save),
    path('admin/hawala/mudeeriath/add/',views_mudeeriath.mudeeriath_form,name='mudeeriath_form'),
    path('admin/hawala/mudeeriath/add/<str:update_id>',views_mudeeriath.mudeeriath_form),
    path('admin/', admin.site.urls),
    
]

urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)