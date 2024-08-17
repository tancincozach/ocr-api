from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from .customer_model import Customers
from .customer_serializer import CustomerSerializer

class BaseViewMixin:
    """
    Mixin to handle common exception handling for all views.
    """
    def handle_exception(self, request, method, *args, **kwargs):
        try:
            return method(request, *args, **kwargs)
        except APIException as e:
            return Response({'detail': str(e)}, status=e.status_code)
        except Exception as e:
            return Response({'detail': 'An unexpected error occurred. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CustomerListCreateView(BaseViewMixin, generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.handle_exception(request, self.list, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.handle_exception(request, self.create, *args, **kwargs)

class CustomerRetrieveDeleteView(BaseViewMixin, generics.RetrieveDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.handle_exception(request, self.retrieve, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.handle_exception(request, self.destroy, *args, **kwargs)
