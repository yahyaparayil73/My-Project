from django.urls import path
from .import views
app_name = 'ecomapi'

urlpatterns = [
    
    path('ecomapi_add',views.add_student,name='ecomapi_add'),
    path('ecomapi_view',views.view_student,name='ecomapi_view'),
    path('ecomapi_delete/<int:sid>',views.delete_student,name='ecomapi_delete'),
    path('ecomapi_update/<int:sid>',views.update_student,name='ecomapi_update'),

]