from django.urls import path
from orderapp import views


app_name='orderapp'

urlpatterns = [
    path('', views.OrderList.as_view(), name='order_list'),
    path('create/', views.OrderItemsCreate.as_view(), name='order_create'),
]