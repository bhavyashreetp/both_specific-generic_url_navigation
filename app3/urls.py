from django.urls import path
from app3.views import * 

app_name='app3'

urlpatterns=[
    path('sri/',sri,name='sri'),
    path('chutki/',chutki,name='chutki'),



]