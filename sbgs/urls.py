from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello,name = 'SBGS'),
     
   
]
urlpatterns += staticfiles_urlpatterns()