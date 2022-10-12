from django.shortcuts import render


def admin_login(request):
    return render(request,'common/admin login.html')

def customer_login(request):
    return render(request,'common/customer login.html')

def customer_signup(request):
    return render(request,'common/customer signup.html')

def project_home(request):
    return render(request,'common/project home.html')

def seller_login(request):
    return render(request,'common/seller login.html')

def seller_signup(request):
    return render(request,'common/seller signup.html') 