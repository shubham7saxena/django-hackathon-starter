"""
URLconf for registration and activation, using django-registration's
default backend.

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.

If you'd like to customize registration behavior, feel free to set up
your own URL patterns for these views instead.

"""


from django.conf.urls import include
from django.conf.urls import url
from django.conf import settings
from django.views.generic.base import TemplateView

from .views import ActivationView
from .views import RegistrationView
from .views import ResendActivationView


urlpatterns = [
    url(r'^activate/(?P<activation_key>\w+)/$',
        ActivationView.as_view(),
        name='registration_activate'),
    url(r'^register/complete/$',
        TemplateView.as_view(template_name='registration/registration_complete.html'),
        name='registration_complete'),
    url(r'^register/closed/$',
        TemplateView.as_view(template_name='registration/registration_closed.html'),
        name='registration_disallowed'),
]

if getattr(settings, 'INCLUDE_REGISTER_URL', True):
    urlpatterns += [
        url(r'^register/$',
            RegistrationView.as_view(),
            name='registration_register'),
    ]

if getattr(settings, 'INCLUDE_AUTH_URLS', True):
    urlpatterns += [
        url(r'', include('registration.auth_urls')),
    ]
