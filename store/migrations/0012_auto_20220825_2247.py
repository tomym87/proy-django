# Generated by Django 3.2.10 on 2022-08-25 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20220825_2114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prod_ficha',
            new_name='prod_fichas',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='prod_precios',
            new_name='prod_precio',
        ),
    ]
