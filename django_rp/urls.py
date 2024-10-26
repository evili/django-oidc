from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
                       # URLS for OpenId authentication
                       re_path(r'openid/', include('djangooidc.urls')),

                       # Test URLs
                       re_path(r'^$', 'testapp.views.home', name='home'),
                       re_path(r'^unprotected$', 'testapp.views.unprotected', name='unprotected'),

                       # Uncomment the next line to enable the admin:
                       re_path(r'^admin/', include(admin.site.urls)),

                ]
