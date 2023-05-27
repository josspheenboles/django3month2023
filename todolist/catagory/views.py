from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def CatagoryList(requ):
    return HttpResponse('CatagoryList')
def CatagoryAdd(requ):
    return render(requ,'catagory/add.html')#HttpResponse('CatagoryAdd')
def Catagoryupdate(requ,id):
    return HttpResponse('Catagoryupdate')

def CatagoryDelete(requ,ID):
    return HttpResponse('CatagoryDelete')
