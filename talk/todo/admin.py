# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import TodoList, TodoItem

admin.site.register(TodoList)
admin.site.register(TodoItem)
