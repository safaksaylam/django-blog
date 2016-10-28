from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),

    url(r'', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
