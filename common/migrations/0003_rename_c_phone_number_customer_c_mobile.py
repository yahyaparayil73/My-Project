# Generated by Django 4.1.7 on 2023-03-07 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_customer_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='c_phone_number',
            new_name='c_mobile',
        ),
    ]
