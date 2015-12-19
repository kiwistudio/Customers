from django.conf.urls import patterns, include, url
from orderlist_app.views import EditOrderView

urlpatterns = patterns('',
	url(r'^$', 'orderlist_app.views.home', name='home'),
	url(r'^order/add/customer/$', 'orderlist_app.views.add_order', name='add_order'),
	url(r'^order/add/customer/orderlist/(?P<pk>\d+)/$', 'orderlist_app.views.orderlist', name='orderlist'),
	url(r'^order/edit/(?P<pk>\d+)/$', EditOrderView.as_view(), name='edit_order'),

)

