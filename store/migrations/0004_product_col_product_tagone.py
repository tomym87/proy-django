# Generated by Django 4.0.4 on 2022-05-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_product_col_remove_product_tagone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='col',
            field=models.CharField(default='bg-primary', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tagone',
            field=models.CharField(default='PE4710', max_length=100, unique=True),
        ),
    ]
