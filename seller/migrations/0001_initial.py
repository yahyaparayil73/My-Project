# Generated by Django 4.1.3 on 2023-01-11 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0005_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.CharField(max_length=100)),
                ('product_category', models.CharField(max_length=50)),
                ('product_no', models.BigIntegerField()),
                ('product_stock', models.IntegerField()),
                ('product_price', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='product/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
            options={
                'db_table': 'product_tb',
            },
        ),
    ]
