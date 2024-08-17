from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from .customer_model import Customers
from .customer_serializer import CustomerSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except APIException as e:
            # APIException provides more specific errors related to the API
            return Response({'detail': str(e)}, status=e.status_code)
        except Exception as e:
            # Generic exception for unexpected errors
            return Response({'detail': 'An unexpected error occurred. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            return self.create(request, *args, **kwargs)
        except APIException as e:
            return Response({'detail': str(e)}, status=e.status_code)
        except Exception as e:
            return Response({'detail': 'An unexpected error occurred. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
