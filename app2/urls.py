from django.urls import path
from app2.views import *

app_name='app2'
urlpatterns=[
        path('bhavya/',bhavya,name='bhavya'),
        path('jerry/',jerry,name='jerry'),





]