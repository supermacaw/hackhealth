#from django.conf.urls import patterns, include, url
#from django.http import HttpResponseRedirect
#from main.views import front_page, home_page
from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from main.views import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


#generic views
urlpatterns = patterns('main.views',
    url(r'^', 'front_page'),#the first page
    url(r'^home/$', 'home_page'),#the personalized home page with Notifications etc
    url(r'^about/$', 'about'),#about page
)
