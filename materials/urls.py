from django.conf.urls import url,include
from materials import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name = 'user-detail'),
    url(r'^polymers/$', views.PolymerList.as_view(),name ='polymer-list'),
    url(r'^polymers/(?P<pk>[0-9]+)/$', views.PolymerDetail.as_view(), name ='polymer-detail'),
    url(r'^producers/$', views.ProducerList.as_view(), name ='producer-list'),
    url(r'^producers/(?P<pk>[0-9]+)/$', views.ProducerDetail.as_view(), name ='producer-detail'),
    url(r'^products/$', views.ProductList.as_view(), name ='product-list'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name = 'product-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]