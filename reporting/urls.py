from django.urls import include, path
from rest_framework.routers import DefaultRouter
from reporting.views import OrderViewSet, CategoryViewSet, CustomerViewSet, SupplierViewSet, ProductViewSet, CountryFilterViewSet, CityFilterViewSet, ProductFilterViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='orders')
router.register('categories', CategoryViewSet, basename='categories')
router.register('customers', CustomerViewSet, basename='customers')
router.register('suppliers', SupplierViewSet, basename='suppliers')
router.register('products', ProductViewSet, basename='products')
router.register('country-filters', CountryFilterViewSet, basename='country-filters')
router.register('city-filters', CityFilterViewSet, basename='city-filters')
router.register('product-filters', ProductFilterViewSet, basename='product-filters')

urlpatterns = [
    path('', include(router.urls))
]