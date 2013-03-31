from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'fdiary.views.home', name='home'),
    url(r'^$', 'fnotes.views.index', name='fnotes_index'),
    url(r'^new/$', 'fnotes.views.edit', name='fnotes_new'),
    url(r'^detail/(?P<entry_id>\d+)/$', 'fnotes.views.detail', name='fnotes_detail'),
    url(r'^detail/(?P<entry_id>\d+)/edit/$', 'fnotes.views.edit', name='fnotes_edit'),
    url(r'^tag/(?P<tag_id>\d+)/$', 'fnotes.views.tag', name='fnotes_tag'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
