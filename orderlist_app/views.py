# _*_ coding: utf-8 _*_ #

import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Customer, Product

# Create your views here.
def home(request):
	return render(request, 'home.html')


def add_order(request):
	if request.method == "POST":
		# was form add button clicked?

		if request.POST.get('ok') is not None:

			# errors collection
			errors = {}

			# validate student data will go here
			data = {}
			
			# validate user input
			first_name = request.POST.get('first_name', '').strip()
			if not first_name:
				errors['first_name'] = u"Поле обязательно"
			else:
				data['first_name'] = first_name

			last_name = request.POST.get('last_name', '').strip()
			if not last_name:
				errors['last_name'] = u"Поле обязательно"
			else:
				data['last_name'] = last_name

			adress = request.POST.get('adress', '').strip()
			if not adress:
				errors['adress'] = u"Поле обязательно"
			else:
				data['adress'] = adress

			phone = request.POST.get('phone', '').strip()
			if not phone:
				errors['phone'] = u"Поле обязательно"
			else:
				data['phone'] = phone
				
			# save customer
			if not errors:
				customer = Customer(**data)
				customer.save()	
				messages.success(request, u'Заказчик %s %s добавлен!' % (data['first_name'], data['last_name']))
				return HttpResponseRedirect(reverse('add_order2'))
			else:
				# render form with errors and previous user input
				return render(request, 'add_order.html', {'errors': errors})

		elif request.POST.get('exit') is not None:
			# redirect to home page on cancel button
			messages.info(request, u'Заказ отменен!')
			return HttpResponseRedirect(u'%s' % reverse('home'))
	else:
		# initial form render
		return render(request, 'add_order.html')


def add_order2(request):
	if request.method == "POST":
		# was form add button clicked?

		if request.POST.get('ok') is not None:

			# errors collection
			errors = {}

			# validate student data will go here
			data = {}
			
			# validate user input
			product_name = request.POST.get('product_name', '').strip()
			if not product_name:
				errors['product_name'] = u"Поле обязательно"
				data['product_name'] = product_name

			price = request.POST.get('price', '').strip()
			if not price:
				errors['price'] = u"Поле обязательно"
			else:
				data['price'] = price

			quantity = request.POST.get('quantity', '').strip()
			if not quantity:
				errors['quantity'] = u"Поле обязательно"
			else:
				data['quantity'] = quantity
				
			# save product
			if not errors:
				product = Product(**data)
				product.save()	
				messages.success(request, u'Продукт %s добавлен!' % (data['product_name']))
				return HttpResponseRedirect(reverse('orderlist'))
			else:
				# render form with errors and previous user input
				return render(request, 'add_order2.html', {'errors': errors})

		elif request.POST.get('exit') is not None:
			# redirect to home page on cancel button
			messages.info(request, u'Заказ отменен!')
			return HttpResponseRedirect(u'%s' % reverse('home'))
	else:
		# initial form render
		return render(request, 'add_order2.html')


def orderlist(request, pk):
	customer = Customer.objects.get(pk=pk)
	product = Product.objects.filter(customer_foreign=pk)
	now_date = datetime.date.today()

	# paginate operations
	paginator = Paginator(customer, 20)
	page = request.GET.get('page')
	try:
		customer = paginator.page(page)
		customer = Customer.objects.get(pk=pk)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		customer = paginator.page(1)
	except EmptyPage:
	# last page of results.
		customer = customer.objects.get(pk=pk)
		customer = paginator.page(paginator.num_pages)

	context = {'customer':customer,
			'now_date':now_date,
			'product':product}

	if request.method == "POST":
		if request.POST.get('exit') is not None:
			return HttpResponseRedirect(reverse('home'))
	return render(request, 'orderlist.html', context)
	