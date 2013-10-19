from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


#generic views
urlpatterns = patterns('main.home_views',
    url(r'^$', 'front_page'),#the first page
    url(r'^home/$', 'home_page'),#the personalized home page with Notifications etc
    url(r'^about/$', 'about'),#about page
)




urlpatterns = patterns('',
	url(r'^$', 'front_page'),#the first page

    # Examples:
    # url(r'^$', 'hackhealth.views.home', name='home'),
    # url(r'^hackhealth/', include('hackhealth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
