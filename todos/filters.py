import django_filters
from .models import Todo

class TodoFilter(django_filters.FilterSet):
    category = django_filters.ChoiceFilter(choices=Todo.CATEGORY_CHOICES)

    class Meta:
        model = Todo
        fields = ['category']
