from django.conf.urls import patterns, include, url
from bsc import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^index/$', views.main, name='main'),
	url(r'^mision/$', views.showMision, name='showMision'),
	url(r'^perspectiva/$', views.showPerspectiva, name='showPerspectiva'),
    url(r'^envio-mision/$', views.ingresarMision, name='ingresarMision'),
    url(r'^perspectiva/cargar_perspectivas/$', views.loadPerspectiva, name='loadPerspectiva'),
    url(r'^perspectiva/editar_perspectivas/$', views.editPerspectiva, name='editPerspectiva'),
    #url(r'^estrategias/$', views.showEstrategia, name='showEstrategia'),
    url(r'^categoria/$', views.showCategoria, name='showCategoria'),
    url(r'^categoria/cargar_categorias/$', views.loadCategorias, name='loadCategorias'),
    url(r'^categoria/editar_categorias/$', views.editarCategoria, name='ingresarCategoria'),
    url(r'^unidad_medida/$', views.showUnidad, name='showUnidad'),  
    url(r'^unidad_medida/cargar_unidades/$', views.loadUnidades, name='loadUnidades'),
    url(r'^unidad_medida/editar_unidades/$', views.editarUnidad, name='editarUnidad'),
    url(r'^indicador/$', views.showIndicador, name='showInidicador'),  
    url(r'^indicador/cargar_indicadores/$', views.loadIndicadores, name='loadIndicadores'),
    url(r'^indicador/cargar_unidades/$', views.loadSelectUnidades, name='loadSelectUnidades'),
    url(r'^indicador/cargar_categorias/$', views.loadSelectCategorias, name='loadSelectCategorias'),
    url(r'^indicador/editar_indicadores/$', views.editIndicador, name='editIndicador'),
    url(r'^ingresar_indicadores_categorias/$', views.ingresarCategoriasXIndicador, name='ingresarCategoriasXIndicador'),
    url(r'^ingresar_indicadores_categorias/cargar_categorias/$', views.loadCategorias, name='loadCategorias'),
    url(r'^estrategia/$', views.showEstrategia, name='showEstrategia'),
    url(r'^cargar_perspectivas/$', views.loadSelectPerspectivas, name='loadSelectPerspectivas'),
    url(r'^cargar_categorias/$', views.loadSelectCategoria, name='loadSelectCategoria'),
    url(r'^load_indicadores_tipo/$', views.loadSelectCategoriaTipo, name='loadSelectCategoriaTipo'),


    # Examples:
    # url(r'^$', 'bsc_gpa.views.home', name='home'),
    # url(r'^bsc_gpa/', include('bsc_gpa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
