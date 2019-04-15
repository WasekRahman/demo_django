from django.conf.urls import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^details/(?P<id>\d+)/$',views.details,name='details'),
    url(r'^login/$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^test/$', views.test, name='test'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()