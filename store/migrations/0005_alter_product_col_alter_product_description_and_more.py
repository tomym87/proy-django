# Generated by Django 4.0.4 on 2022-05-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_col_product_tagone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='col',
            field=models.CharField(default='bg-primary', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='tagone',
            field=models.CharField(default='PE4710', max_length=100),
        ),
    ]
