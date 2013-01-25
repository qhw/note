from django.conf.urls import patterns, include, url
from things.views import note, pagination, kindeditor, test
from django.contrib.auth.views import login, logout
import our.settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'our.views.home', name='home'),
    # url(r'^our/', include('our.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$',   note.note_show),
    url(r'^subjects/$',   note.note_subjects),
    url(r'^one/$',   note.note_get),
    url(r'^create/$', note.note_create),
    url(r'^update/$', note.note_update),
    url(r'^del/$', note.note_delete),
    
    url(r'^numbers/$', pagination.note_total_number),
    url(r'^page/$', pagination.note_page),
    url(r'^pagination/$', pagination.pagination),
    
    url(r'^upload/$', kindeditor.ke_upload_view),
    url(r'^file_manager_json/$', kindeditor.file_manager_json),
    
    url(r'^css/(?P<path>.*)$','django.views.static.serve',  
                         {'document_root':our.settings.TEMPLATE_DIRS[0] + "/css/"}),
    url(r'^js/(?P<path>.*)$','django.views.static.serve',  
                         {'document_root':our.settings.TEMPLATE_DIRS[0]+"/js/"}),
    url(r'^kindeditor/(?P<path>.*)$','django.views.static.serve',  
                         {'document_root':our.settings.TEMPLATE_DIRS[0]+"/kindeditor/"}),
    url(r'^attached/(?P<path>.*)$','django.views.static.serve',  
                         {'document_root':our.settings.TEMPLATE_DIRS[0]+"/attached/"}),
    url(r'^img/(?P<path>.*)$','django.views.static.serve',  
                         {'document_root':our.settings.TEMPLATE_DIRS[0]+"/img/"}),
                       
    url(r'^test/$', test.test),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/profile/$',   note.note_show),

)
