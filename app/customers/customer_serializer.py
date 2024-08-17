from rest_framework import serializers
from .customer_model import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['first_name', 'last_name', 'email', 'address', 'created', 'deleted_at']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'address': {'required': True},
            'created': {'read_only': False},  # Set 'created' field to read-only
            'deleted_at': {'required': False},  # Allow 'deleted_at' to be optional
        }
