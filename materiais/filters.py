import django_filters
from .models import Material 

class SnippetFilter(django_filters.FilterSet):
    class Meta:
        model = Material
        fields = ('titulo', 'desc', 'created_date')