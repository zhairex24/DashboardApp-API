from rest_framework import viewsets

from reporting.models import Order, Category, Customer, Supplier, Product
from reporting.serializers import OrderSerializer, CategorySerializer, CustomerSerializer, SupplierSerializer, ProductSerializer
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by('-order_date')
    
class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CustomerViewSet(viewsets.ModelViewSet):

    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all().order_by('province', 'last_name')
    

class SupplierViewSet(viewsets.ModelViewSet):

    serializer_class = SupplierSerializer

    def get_queryset(self):
        return Supplier.objects.all().order_by('province', 'company_name')

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = ProductSerializer