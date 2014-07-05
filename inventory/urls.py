from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inventory.views.home', name='home'),
    # url(r'^inventory/', include('inventory.foo.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home_page"),
    url(r'^components/$', 'components.views.components_page', name='component_list_page'),
    url(r'^components/add/$', 'components.views.component_add_page', name='component_add_page'),
    url(r'^component/(?P<pk>.+)/edit/$', 'components.views.component_edit_page', name='component_edit_page'),
    url(r'^component/(?P<pk>.+)/delete/$', 'components.views.component_delete_page', name='component_delete_page'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                           )
