import django_filters
from .models import Product,ProductBySize
class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = Product
        fields = ('price', 'id') 
