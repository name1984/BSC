from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^home$', 'bscard.views.runBsc'),
                       (r'^ingreso$', 'bscard.views.addKpi'),
                       (r'^mision$', 'bscard.views.addMision'),
                       (r'^perspectiva$', 'bscard.views.addPerspective')
                       
    # Examples:
    # url(r'^$', 'bsc.views.home', name='home'),
    # url(r'^bsc/', include('bsc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
