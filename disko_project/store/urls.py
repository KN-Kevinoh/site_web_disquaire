#import urls from project
from django.conf.urls import url

#import views 
from . import views

urlpatterns = [
    #url(r'^$', views.index), # /store may call method index (view) 
    url(r'^$', views.listing, name='listing'), # /store may call method listing (view)
    url(r'^(?P<id>[0-9]+)/$', views.details, name='details'),
    url(r'^search/$', views.search, name='search'),
]