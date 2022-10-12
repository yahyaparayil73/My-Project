from django.urls import path
from . import views
app_name='customer'
urlpatterns=[
    path('chome',views.customer_home,name='home'),
    path('ccheckout',views.customer_checkout,name='checkout'),
    path('cmycart',views.customer_mycart,name='mycart'),
    path('cchangepassword',views.customer_changepassword,name='changepassword'),
    path('cproductdetails',views.customer_productdetails,name='productdetails'),
    path('cprofile',views.customer_profile,name='profile'),
    path('cmyorders',views.customer_myorders,name='myorders'),
    

]