from django.shortcuts import render
from .models import Product
from common.models import Seller


def add_product(request):
    if request.method == 'POST':
        p_name = request.POST['p_name']
        p_description = request.POST['p_description']
        p_category = request.POST['p_category']
        p_no = request.POST['p_no']
        p_stock = request.POST['p_stock']
        p_price = request.POST['p_price']
        p_image = request.FILES['p_image']
        seller = request.session['seller']
        new_products = Product(
            product_name = p_name,
            product_description = p_description,
            product_category = p_category,
            product_no = p_no,
            product_stock = p_stock,
            product_price = p_price,
            product_image = p_image,
            seller_id = seller)
        new_products.save()

    return render(request, 'seller/add product.html')


def change_password(request):
    error_msg = ''
    success_msg = ''
    if request.method == "POST":
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password == confirm_password:
            if len(new_password) > 8:
                seller = Seller.objects.get(id=request.session['seller'])
                if old_password == seller.password:
                    seller.password = new_password
                    seller.save()
                    success_msg = 'updated successfully'
            else:
                error_message = 'password should be minimum 8 characters'
        else:
            error_message = 'password does\'nt match'
    return render(request, 'seller/change password.html',{'error': error_msg,'success' : success_msg})


def seller_home(request):
    return render(request, 'seller/seller home.html')


def product_catalogue(request):
    return render(request, 'seller/product catalogue.html')


def seller_profile(request):
    seller_details = Seller.objects.get(id = request.session['seller'])
    return render(request, 'seller/seller profile.html',{'seller_profile':seller_details})


def update_stock(request):
    return render(request, 'seller/update stock.html')

def view_product(request):
    product = Product.objects.filter(seller_id = request.session['seller'])
    return render(request, 'seller/view_product.html',{'products': product})


def view_orders(request):
    return render(request, 'seller/view orders.html')

def javascript_sample(request):
    return render(request, 'seller/javascriptsample.html')

def master_seller(request):
    return render(request, 'seller/master_seller.html')