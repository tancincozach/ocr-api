# app/users/urls.py
from django.urls import path
from .customer_view import CustomerListCreateView, CustomerRetrieveDeleteView

urlpatterns = [
    path('', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customer/<int:id>/', CustomerRetrieveDeleteView.as_view(), name='customer-detail'),
]
