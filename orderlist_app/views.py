# _*_ coding: utf-8 _*_ #

import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib import messages

from django.forms import ModelForm
from django.views.generic import UpdateView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

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


			data2 = {}

			product_name = request.POST.get('product_name', '').strip()
			if not product_name:
				errors['product_name'] = u"Поле обязательно"
			else:
				data2['product_name'] = product_name

			price = request.POST.get('price', '').strip()
			if not price:
				errors['price'] = u"Поле обязательно"
			else:
				data2['price'] = price

			quantity = request.POST.get('quantity', '').strip()
			if not quantity:
				errors['quantity'] = u"Поле обязательно"
			else:
				data2['quantity'] = quantity

			data2['data_create'] = datetime.date.today()
			data2['data_change'] = datetime.date.today()
				
			# save customer
			if not errors:
				customer = Customer(**data)
				customer.save()	
				product = Product(**data2)
				product.save()
				messages.success(request, u'Заказчик %s %s добавлен!' % (data['first_name'], data['last_name']))
				return HttpResponseRedirect(u'orderlist/%s/' % str(customer.id))
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


class EditOrderForm(ModelForm):

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'adress', 'phone']

    def __init__(self, *args, **kwargs):
	    super(EditOrderForm, self).__init__(*args, **kwargs)

	    self.helper = FormHelper(self)

	        # set form tag attributes
	    self.helper.form_action = reverse('edit_order', kwargs={'pk': kwargs['instance'].id})
	    self.helper.form_method = 'POST'
	    self.helper.form_class = 'form-horizontal'

	        # set form field properties
	    self.helper.help_text_inline = True
	    self.helper.html5_required = True
	    self.helper.label_class = 'col-sm-2 control-label'
	    self.helper.field_class = 'col-sm-10'

	        # add buttons
	    self.helper.layout[-1] = FormActions(
	        Submit('add_button', u'Сохранить', css_class="btn btn-primary"),
	        Submit('cancel_button', u'Отменить', css_class="btn btn-link"),
	    )    

class EditOrderForm2(ModelForm):

    class Meta:
        model = Product
        fields = ['product_name', 'price', 'quantity']

    def __init__(self, *args, **kwargs):
	    super(EditOrderForm2, self).__init__(*args, **kwargs)

	    self.helper = FormHelper(self)

	        # set form tag attributes
	    self.helper.form_action = reverse('edit_order', kwargs={'pk': kwargs['instance'].id})
	    self.helper.form_method = 'POST'
	    self.helper.form_class = 'form-horizontal'

	        # set form field properties
	    self.helper.help_text_inline = True
	    self.helper.html5_required = True
	    self.helper.label_class = 'col-sm-2 control-label'
	    self.helper.field_class = 'col-sm-10'

	        # add buttons
	    # self.helper.layout[-1] = FormActions(
	    #     Submit('add_button', u'Сохранить', css_class="btn btn-primary"),
	    #     Submit('cancel_button', u'Отменить', css_class="btn btn-link"),
	    # ) 


class EditOrderView(UpdateView):
	model = Customer, Product
	template_name = 'edit_order.html'
	form_class = EditOrderForm
	def get_success_url(self):
		return u'%s?status_message=Заказ сохранен!' % reverse('edit_order')
	def post(self, request, *args, **kwargs):
		if request.POST.get('cancel_button'):
			return HttpResponseRedirect(u'%s?status_message=редактирование отменено!' % reverse('edit_order'))
		else:
			return super(EditOrderView, self).post(request, *args, **kwargs)

def orderlist(request, pk):
	customer = Customer.objects.get(pk=pk)
	product = Product.objects.get(customer_foreign=pk)

	# paginate operations
	# paginator = Paginator(customer, 20)
	# page = request.GET.get('page')
	# try:
	# 	customer = paginator.page(page)
	# 	customer = Customer.objects.get(pk=pk)
	# except PageNotAnInteger:
	# # If page is not an integer, deliver first page.
	# 	customer = paginator.page(1)
	# except EmptyPage:
	# # last page of results.
	# 	customer = Customer.objects.get(pk=pk)
	# 	customer = paginator.page(paginator.num_pages)

	context = {'customer':customer,
			'product':product}

	if request.method == "POST":
		if request.POST.get('exit') is not None:
			return HttpResponseRedirect(reverse('home'))
	return render(request, 'orderlist.html', context)
	