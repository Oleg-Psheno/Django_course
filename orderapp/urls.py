from django.urls import path
from orderapp import views


app_name='ordersapp'

urlpatterns = [
    path('', views.OrderList.as_view(), name='order_list'),

]