from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^round1/$', views.Round1View.as_view(), name='round1'),
    url(r'^round2/$', views.Round2View.as_view(), name='round2'),
    url(r'^round3/$', views.Round3View.as_view(), name='round3'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]
