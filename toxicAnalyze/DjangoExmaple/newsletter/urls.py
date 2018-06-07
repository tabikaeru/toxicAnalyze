from django.conf.urls import url, include
from newsletter import views


app_name = 'genericviews'

urlpatterns = [
    url(r'^', views.signupform, name='signupform'),]
