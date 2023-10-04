from . import views 
from django.urls import path 

urlpatterns = [
  
  path("",views.home , name="home"),
  path("error",views.error , name="error"),
  path("contact",views.contact , name="contact"),
  path("contact",views.contact , name="contact"),
  path("reservation",views.reservation , name="reservation"),
  path("coffee",views.coffee , name="coffee"),        
]
