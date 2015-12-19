# _*_ coding: utf-8 _*_ #

from django.db import models

# Create your models here.
class Customer(models.Model):
    """Customer"""

    class Meta(object):
        verbose_name = u'Заказчик'
        verbose_name_plural = u"Заказчики"
        ordering = ('last_name',) # sorted by lats_name (default)

	# Добавляем метод для удобного представления в shell и Django админке
    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
			

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Имя")

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Фамилия")

    adress = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Адрес")

    phone = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"телефон")


class Product(models.Model):
    """Product"""

    class Meta(object):
        verbose_name = u'товар'
        verbose_name_plural = u"товары"
        ordering = ('product_name',) # sorted by product_name (default)

	# Добавляем метод для удобного представления в shell и Django админке
    def __unicode__(self):
        return u"%s" % (self.product_name)
			

    product_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Наименование")

    price = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"цена")

    quantity = models.IntegerField(
        blank=False,
        default=0,
        verbose_name=u"колличество")

    data_create = models.CharField(
        max_length=256,
        blank=False,
        null=True,
        verbose_name=u"Дата и время операции")

    data_change = models.CharField(
        max_length=256,
        blank=False,
        null=True,
        verbose_name=u"Дата и время операции")

    customer_foreign = models.ForeignKey('Customer',
    	blank=False,
        null=True,
        verbose_name=u"Заказчик")