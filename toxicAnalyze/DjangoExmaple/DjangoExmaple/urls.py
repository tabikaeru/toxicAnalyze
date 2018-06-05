from django.conf.urls import url, include
from django.contrib import admin
 
#importing views from newsletter app
from newsletter.templates import views as newsletter_views


urlpatterns = [
 #defining url for form
    url(r'^signup/', newsletter_views.signupform),

    url(r'^textAnalyze/', newsletter_views.signupform),

    url(r'^admin/', admin.site.urls),

    url(r'^home/', newsletter_views.signupform),

    url(r'^', include("newsletter.urls")),

]


