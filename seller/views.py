from django.shortcuts import render

def add_product(request):
    return render(request,'seller/add product.html')

def change_password(request):
    return render(request,'seller/change password.html')

def seller_home(request):
    return render(request,'seller/home.html')

def product_catalogue(request):
    return render(request,'seller/product catalogue.html')

def seller_profile(request):
    return render(request,'seller/seller profile.html')

def update_stock(request):
    return render(request,'seller/ update stock.html')

def view_orders(request):
    return render(request,'seller/view orders.html')