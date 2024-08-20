from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from .filters import TodoFilter

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_class = TodoFilter
