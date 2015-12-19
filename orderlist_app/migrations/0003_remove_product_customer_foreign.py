# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderlist_app', '0002_product_customer_foreign'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='customer_foreign',
        ),
    ]
