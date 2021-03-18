from django.shortcuts import render
from django.views.generic import ListView
from .models import Order, OrderItem



class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


