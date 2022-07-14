from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello,name = 'SBGS'),
    url(r'^media/(?P<path>.*)$',{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', {'document_root': settings.STATIC_ROOT}), 
   
]
urlpatterns += staticfiles_urlpatterns()