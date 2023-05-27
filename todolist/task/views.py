from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
#view python function must accept httprequest as object ,return httpresponse as object
def tasklist(request):
    tasks=[(1,'task1'),(2,'task2'),(3,'task3')]
    context={}
    context['tasks']=tasks
    return  render(request,'task/list.html',context)#HttpResponse('hi from task list view')

def taskadd(req):
    return  render(req,'task/add.html') #HttpResponse('hi from add task view')
def taskupdate(req,id):
    return HttpResponseRedirect('/Tasks') #HttpResponse('hi from Updaate task view')

def taskDelete(request,ID):
    return  HttpResponse('hi id ='+str(ID)+' deleted')