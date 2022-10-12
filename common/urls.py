from django.urls import path
from . import views

urlpatterns=[
    path('comadminlogin',views.admin_login),
    path('customerlogin',views.customer_login),
    path('customersignup',views.customer_signup),
    path('projecthome',views.project_home),
    path('sellerlogin',views.seller_login),
    path('sellersignup',views.seller_signup),
    

]