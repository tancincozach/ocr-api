# app/users/urls.py
from django.urls import path
from .customer_list_create_view import CustomerListCreateView

urlpatterns = [
    path('', CustomerListCreateView.as_view(), name='customer-list-create'),
]
