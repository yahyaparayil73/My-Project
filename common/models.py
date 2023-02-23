from django.db import models

# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    
    class Meta: 
        db_table = 'customer_tb'


class Seller(models.Model):
    name = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    user_name = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=30)
    bank_branch = models.CharField(max_length=40)
    ifsc_code = models.CharField(max_length=20)
    seller_pic = models.ImageField(upload_to='seller/')

    class Meta:
        db_table = 'seller_tb'

    