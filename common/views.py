from django.core.mail import send_mail
from django.conf import settings
from random import randint
from django.shortcuts import render,redirect
from common.models import Customers
from common.models import Seller
from django.http import JsonResponse


def admin_login(request):
    return render(request, 'common/admin login.html')


def customer_login(request):
    msg = ''
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            customer = Customers.objects.get(
                email=email, password=password)  # model_name= post_name
            request.session['customer'] = customer.id
            return redirect('customer:home')  # redirect(app_name:url_name)
        except Exception as e:
            print(e)  # to check error
            msg = 'Invalid credentials'

    return render(request, 'common/customer login.html', {'message': msg})


def customer_signup(request):
    if request.method == "POST":
        name = request.POST['your_name']
        mobile_number = request.POST['mobile_number']
        email = request.POST['email']
        password = request.POST['password']
        new_customer = Customers(
            name=name, mobile_number=mobile_number, email=email, password=password)
        new_customer.save()  # corresponding query of insert
    return render(request, 'common/customer signup.html')


def project_home(request):
    return render(request, 'common/project home.html')


def seller_login(request):

    msg = ''
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST["password"]
        try:
            seller = Seller.objects.get(user_name = user_name,password = password)
            request.session['seller'] = seller.id
            return redirect('seller:seller_home')
        except Exception as e:
            print (e)
            msg = 'Invalid credentials'

    return render(request, 'common/seller login.html',{'message':msg})


def seller_signup(request):
    msg = ''
    if request.method == "POST":
        name = request.POST['seller_name']
        mobile_number = request.POST['seller_mobile']
        email = request.POST['seller_email']
        # password = request.POST['seller_password']
        bank_name = request.POST['seller_bank_name']
        bank_branch = request.POST['seller_bank_branch']
        ifsc_code = request.POST['seller_ifsc']
        seller_pic = request.FILES['seller_pic']

        user_name = randint(1111, 9999)
        password = 'sell-' + str(user_name) + '-' + mobile_number[6:10]
        new_seller = Seller(
            name=name,
            mobile_number=mobile_number,
            email=email,
            password=password,
            bank_name=bank_name,
            bank_branch=bank_branch,
            ifsc_code=ifsc_code,
            user_name=user_name,
            seller_pic=seller_pic
        )
        msg = 'Account has been created successfully'
        email_subject = 'Account username and password'
        email_content = 'Hai your username will be ' + \
            str(user_name) + 'and password will be ' + password
        send_mail(
            email_subject,
            email_content,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        new_seller.save()

        # corresponding query of insert

    return render(request, 'common/seller signup.html', {'message': msg})

def master_common(request):
    return render(request, 'common/master_common.html')

def js_calculator(request):
    return render(request, 'common/js_calculator.html')

def broto_fb_page(request):
    return render(request, 'common/broto_fb_page.html')

    

     
