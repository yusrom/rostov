#coding: utf-8
from django.conf.urls import *
from django.urls import path, include

from blog.views import PostsListView, PostDetailView 

# urlpatterns = patterns('',
# url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blog/ 
#                                                # будет выводиться список постов
# url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://имя_сайта/blog/число/ 
#                                               # будет выводиться пост с определенным номером

# )
urlpatterns = [
    path(r'$', PostsListView.as_view(), name='list'),
    path(r'(?P<pk>\d+)/$', PostDetailView.as_view()),
]