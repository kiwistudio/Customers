# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderlist_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customer_foreign',
            field=models.ForeignKey(verbose_name='\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a', to='orderlist_app.Customer', null=True),
        ),
    ]
