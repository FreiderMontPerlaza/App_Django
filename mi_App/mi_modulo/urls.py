
from django.urls import path,
from .views import *
from .import views

urlpatterns = [
    path('pagina_1/',views.pagina_1,name=pagina_1),
    path('pagina_2/',views.pagina_2,name=pagina_2),
    path('pagina_3/',views.pagina_3,name=pagina_3),
    
    

]