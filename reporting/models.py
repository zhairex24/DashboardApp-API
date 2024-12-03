from django.db import models

# Create your models here.
GENDER = (
    ['Male', 'Male'],
    ['Female', 'Female'],
    ['Prefere not to say', 'Prefere not to say']
)
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER, default="Prefere not to say")
    barangay = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class Supplier(models.Model):
    company_name = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    barangay = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    webpage = models.CharField(max_length=50)
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Product(models.Model):

    product_name = models.CharField(max_length=100)
    unit_price = models.IntegerField()
    units_in_stock = models.IntegerField()
    units_on_order = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['category', 'unit_price']

class Order(models.Model):
    order_date = models.DateTimeField()
    required_date = models.DateTimeField()
    shipped_name = models.CharField(max_length=100)
    shipped_barangay = models.CharField(max_length=50)
    shipped_city = models.CharField(max_length=50)
    shipped_province = models.CharField(max_length=50)
    shipped_country = models.CharField(max_length=50)
    shipped_postal_code = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)