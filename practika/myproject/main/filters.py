import django_filters
from .models import Service


class PostFilter(django_filters.FilterSet):
    ind = django_filters.CharFilter(field_name='ind')
    name = django_filters.CharFilter(field_name='name')
    price = django_filters.CharFilter(field_name='price')

    class Meta:
        model = Service
        fields = ['ind','name', 'price']