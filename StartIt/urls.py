from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
import accounts.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'StartIt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
)
