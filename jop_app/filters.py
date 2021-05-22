import django_filters
from .models import Jop


class JopFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    # opposite:
    # title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Jop
        fields = '__all__'
        exclude = ['owner', 'image', 'Vacancy', 'slug', 'published_at']
