# Generated by Django 2.0 on 2020-05-21 11:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_botica', '0005_auto_20200521_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carritohasproducto',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='compra',
            options={'managed': True},
        ),
        migrations.AlterField(
            model_name='carrito',
            name='timestap',
            field=models.DateTimeField(blank=True, db_column='Timestap', default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='total',
            field=models.DecimalField(blank=True, db_column='Total', decimal_places=1, max_digits=11, null=True),
        ),
    ]
