from django.conf.urls import url
from . import views



urlpatterns = [

        # url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        # url(r'^(?P<item_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
        url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
        url(r'^suggestions/$', views.suggestions, name='suggestions'),
        url(r'^newitem/$', views.newitem, name='newitem'),
        url(r'^searchlib/$', views.searchlib, name='searchlib'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^myitems/$', views.myitems, name='myitems'),
        url(r'^register/$', views.register, name='register'),
        url(r'^suggestions/(?P<item_id>\d+)/$', views.suggestiondetail, name='suggestiondetail')

]

