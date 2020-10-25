from .serializers import TodoSerializer
from rest_framework import status, viewsets

from .models import Todo
# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.all()
        query_params = self.request.query_params.get('tasks', None)

        if query_params == 'completed':
            return queryset.filter(complete=True)

        return queryset.filter(complete=False)
