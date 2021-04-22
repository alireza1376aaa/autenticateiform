from django.urls import path
from  autentication.views import register_page


app_name='autenticate'

urlpatterns = [

    path('regist',register_page,name='Register'),


]