from django.urls import include, url
from django.contrib import admin

urlpatterns = [
                       # URLS for OpenId authentication
                       url(r'openid/', include('djangooidc.urls')),

                       # Test URLs
                       url(r'^$', 'testapp.views.home', name='home'),
                       url(r'^unprotected$', 'testapp.views.unprotected', name='unprotected'),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                ]
