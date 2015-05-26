# -*- coding: utf-8 -*-

# Django
from django.db import models

from .mixins import SelfPublishModel
from .serializers import TodoListSerializer, TodoItemSerializer


class TodoList(SelfPublishModel, models.Model):
    serializer_class = TodoListSerializer
    channel_name = u"todo-list"

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return u"{name}".format(
            name=self.name,
        )


class TodoItem(SelfPublishModel, models.Model):
    serializer_class = TodoItemSerializer
    channel_name = u"todo-item"

    todo_list = models.ForeignKey(TodoList)
    done = models.BooleanField(default=False)
    text = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{text} ({status})".format(
            text=self.text,
            status=(u"✓" if self.done else u"×")
        )
