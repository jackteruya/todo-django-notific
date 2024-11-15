from rest_framework import serializers

from todo.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = (
            'title',
            'description',
            'completed',
            'start_date',
            'end_date',
        )
