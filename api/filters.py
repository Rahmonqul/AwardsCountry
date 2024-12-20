import django_filters
from .models import Partner

class PartnerFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='award_partners__date', lookup_expr='exact')  # Фильтрация по дате
    award_code = django_filters.CharFilter(field_name='award_partners__award__code', lookup_expr='exact')  # Фильтрация по коду награды
    award_name = django_filters.CharFilter(field_name='award_partners__award__name', lookup_expr='icontains')  # Фильтрация по имени награды (поиск по подстроке)

    class Meta:
        model = Partner
        fields = ['date', 'award_code', 'award_name']



