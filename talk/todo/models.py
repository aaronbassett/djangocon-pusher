# -*- coding: utf-8 -*-

# Django
from django.db import models
# Swamp Dragon
from swampdragon.models import SelfPublishModel
from .serializers import TodoListSerializer, TodoItemSerializer


class TodoList(SelfPublishModel, models.Model):
    serializer_class = TodoListSerializer

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return u"{name}".format(
            name=self.name,
        )


class TodoItem(SelfPublishModel, models.Model):
    serializer_class = TodoItemSerializer

    todo_list = models.ForeignKey(TodoList)
    done = models.BooleanField(default=False)
    text = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{text} ({status})".format(
            text=self.text,
            status=(u"✓" if self.done else u"×")
        )
