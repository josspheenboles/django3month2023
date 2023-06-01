from django.urls import path
from .views import *
urlpatterns = [
    path('',Listcatagory.as_view(),name='CatagoryList'),
    path('Add',Catagoryadding.as_view(),name='CatagoryAdd'),
    path('Update/<int:id>', Listcatagory.as_view(), name='Catagoryupdate'),
    path('Delete/<int:ID>', Listcatagory.as_view(), name='CatagoryDelete'),
    ]