#Blogapp api Url
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns =[
    url(r'^$',views.PostApi.as_view(),name='list'),
    url(r'^create/$',views.PostCreateApi.as_view(),name='create'),
    url(r'^(?P<slug>[\w-]+)/$',views.PostDetailApi.as_view(),name='detail'),
    url(r'^(?P<slug>[\w-]+)/delete/$',views.PostDeleteApi.as_view(),name='delete'),
    url(r'^(?P<slug>[\w-]+)/edit/$',views.PostUpdateApi.as_view(),name='update'),
    url(r'^commentapi/$',views.CommentListApi.as_view(), name= 'comments'),
    url(r'^(?P<slug>[\w-]+)/$',views.CommentDetailApi.as_view(),name='commentdetail'),
]
