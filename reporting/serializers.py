from rest_framework import serializers
from reporting.models import Customer, Order, Category, Supplier, Product

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id',
                  'customer',
                  'order_date',
                  'required_date',
                  'shipped_name',
                  'shipped_barangay',
                  'shipped_city',
                  'shipped_province',
                  'shipped_country',
                  'shipped_postal_code'
                  ]
        
    def to_representation(self, instance):
        self.fields['customer'] = CustomerSerializer(read_only=True)
        self.fields['product'] = ProductSerializer(read_only=True)
        return super(OrderSerializer, self).to_representation(instance)
        
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id',
                  'first_name',
                  'last_name',
                  'gender',
                  'barangay',
                  'city',
                  'province',
                  'country',
                  'postal_code',
                  'phone',
                  'email'
                  ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id',
                  'name',
                  'description'
                  ]

class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = ['id',
                  'company_name',
                  'contact_name',
                  'barangay',
                  'city',
                  'province',
                  'country',
                  'postal_code',
                  'phone',
                  'email',
                  'webpage'
                  ]
        
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id',
                  'product_name',
                  'category',
                  'unit_price',
                  'units_in_stock',
                  'units_on_order'
                  ]
        
    def to_representation(self, instance):
        self.fields['supplier'] = SupplierSerializer(read_only=True)
        self.fields['category'] = CategorySerializer(read_only=True)
        return super(ProductSerializer, self).to_representation(instance)