# Generated by Django 4.0.4 on 2022-05-12 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_rename_cart_cartitem_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='qantity',
            new_name='quantity',
        ),
    ]
