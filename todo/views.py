from rest_framework import viewsets

from todo.models import ToDo
from todo.serializer import ToDoSerializer


class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
