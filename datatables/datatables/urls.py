from django.conf.urls import patterns, include, url
from tables.views import loadTable

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^home$', loadTable, name='loadTable'),
    # Examples:
    # url(r'^$', 'datatables.views.home', name='home'),
    # url(r'^datatables/', include('datatables.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
