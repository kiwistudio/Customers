# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=256, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('adress', models.CharField(max_length=256, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('phone', models.CharField(max_length=256, verbose_name='\u0442\u0435\u043b\u0435\u0444\u043e\u043d')),
            ],
            options={
                'ordering': ('last_name',),
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('price', models.CharField(max_length=256, verbose_name='\u0446\u0435\u043d\u0430')),
                ('quantity', models.IntegerField(default=0, verbose_name='\u043a\u043e\u043b\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('data_create', models.CharField(max_length=256, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438')),
                ('data_change', models.CharField(max_length=256, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438')),
            ],
            options={
                'ordering': ('product_name',),
                'verbose_name': '\u0442\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0442\u043e\u0432\u0430\u0440\u044b',
            },
        ),
    ]
