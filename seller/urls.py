from django.urls import path
from . import views

urlpatterns=[
    path('add product',views.add_product),
    path('change password',views.change_password),
    path('seller home',views.seller_home),
    path('product catalogue',views.product_catalogue),
    path('seller profile',views.seller_profile),
    path('update stock',views.update_stock),
    path('view orders',views.view_orders)

]