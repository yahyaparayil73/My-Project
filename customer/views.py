from django.shortcuts import render


def customer_home(request):
    return render(request,'customer/home.html')

def customer_checkout(request):
    return render(request,'customer/checkout.html')

def customer_mycart(request):
    return render(request,'customer/my cart.html')

def customer_myorders(request):
    return render(request,'customer/my orders.html')

def customer_productdetails(request):
    return render(request,'customer/product details.html')

def customer_changepassword(request):
    return render(request,'customer/change password.html') 

def customer_profile(request):
    return render(request,'customer/profile.html') 
