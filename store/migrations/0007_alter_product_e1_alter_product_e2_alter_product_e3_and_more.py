# Generated by Django 4.0.4 on 2022-05-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_e1_product_e2_product_e3_product_e4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='e1',
            field=models.CharField(default='https://valtic.com.mx', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='e2',
            field=models.CharField(default='https://valtic.com.mx', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='e3',
            field=models.CharField(default='https://valtic.com.mx', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='e4',
            field=models.CharField(default='https://valtic.com.mx', max_length=100),
        ),
    ]
