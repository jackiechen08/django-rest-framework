from django.conf.urls import url
from materials import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #url(r'^$', views.api_root),
    url(r'^polymers/$', views.PolymerList.as_view()),
    url(r'^polymers/(?P<pk>[0-9]+)/$', views.PolymerDetail.as_view()),
    url(r'^producers/$', views.ProducerList.as_view()),
    url(r'^producers/(?P<pk>[0-9]+)/$', views.ProducerDetail.as_view()),
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)