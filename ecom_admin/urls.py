from django.urls import path
from . import views

urlpatterns=[
    path('approve sellers',views.approve_sellers),
    path('ecom home',views.ecom_home),
    path('view customers',views.view_customers),
    path('view sellers',views.view_sellers),

]