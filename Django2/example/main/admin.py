from django.contrib import admin
from .models import Item, ToDoList
# Adds entities to the admin page
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
