from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	# Validations
	url(r'^$', 'orderlist_app.views.home', name='home'),
	url(r'^order/add/customer/$', 'orderlist_app.views.add_order', name='add_order'),
	url(r'^order/add/product/$', 'orderlist_app.views.add_order2', name='add_order2'),
	url(r'^orderlist/$', 'orderlist_app.views.orderlist', name='orderlist'),

)

