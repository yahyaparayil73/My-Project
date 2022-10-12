from django.shortcuts import render

def approve_sellers(request):
    return render(request,'ecom_admin/approve sellers.html')

def ecom_home(request):
    return render(request,'ecom_admin/home.html')

def view_customers(request):
    return render(request,'ecom_admin/view customers.html')

def view_sellers(request):
    return render(request,'ecom_admin/view sellers.html')
