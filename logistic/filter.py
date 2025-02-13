#создаём свой фильтр, который будет искать склад, 
# где есть определённый продукт, 
# но с указанием не id, а части названия или описания

import django_filters

from logistic.models import Stock, Product


class StockFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_by_producr_title_or_description')
    
    class Meta:
        model = Stock
        fields = []
    
    def filter_by_producr_title_or_description (self, queryset, name, value):
        product_ids = Product.objects.filter(positions__product__in=product_ids)