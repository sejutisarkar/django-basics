# to see the views we nees this

from . import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

app_name = 'courses'

urlpatterns = [
url(r'^$', views.course_list),
url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.step_detail),
url(r'(?P<pk>\d+)/$', views.course_detail),

]
