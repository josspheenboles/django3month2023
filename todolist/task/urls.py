from django.urls import path
from .views import *

urlpatterns = [
   path('',tasklist,name='tasklist'),
    path('Add',taskadd,name='taskadd'),
    path('Update/<int:id>',taskupdate,name='taskupdate'),
    path('Delete/<int:ID>',taskDelete,name='taskDelete'),
]
