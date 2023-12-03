from django.urls import path
from . import views_language 
urlpatterns = [
    path('language/list_saved_languages/',views_language.list_saved_languages,name="list_saved_languages"),
    path('language/select_language/',views_language.select_language,name="select_language"),
    path('language/assign_language/<language>',views_language.assign_language,name="assign_language"),
    path('language/insert_language_detail/',views_language.save,name='save_language'),
]
