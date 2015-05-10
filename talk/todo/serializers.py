# -*- coding: utf-8 -*-

# Swamp Dragon
from swampdragon.serializers.model_serializer import ModelSerializer


class TodoListSerializer(ModelSerializer):
    class Meta:
        model = 'todo.TodoList'
        publish_fields = ('name', 'description')


class TodoItemSerializer(ModelSerializer):
    class Meta:
        model = 'todo.TodoItem'
        publish_fields = ('done', 'text')
        update_fields = ('done', )
