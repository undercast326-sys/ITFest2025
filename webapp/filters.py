import django_filters
from .models import University


class UniversityFilter(django_filters.FilterSet):
    tuition_fee_min = django_filters.NumberFilter(field_name='tuition_fee', lookup_expr='gte')
    tuition_fee_max = django_filters.NumberFilter(field_name='tuition_fee', lookup_expr='lte')
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')
    min_unt_score = django_filters.NumberFilter(field_name='min_unt_score', lookup_expr='lte')
    scholarships = django_filters.BooleanFilter(field_name='scholarships')
    internships = django_filters.BooleanFilter(field_name='internships')

    class Meta:
        model = University
        fields = ['city', 'scholarships', 'internships']