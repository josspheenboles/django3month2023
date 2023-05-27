from django.urls import path
from .views import *
urlpatterns = [
    path('',CatagoryList,name='CatagoryList'),
    path('Add',CatagoryAdd,name='CatagoryAdd'),
    path('Update/<int:id>', Catagoryupdate, name='Catagoryupdate'),
    path('Delete/<int:ID>', CatagoryDelete, name='CatagoryDelete'),
    ]