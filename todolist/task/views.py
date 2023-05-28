from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from catagory.models import *
# Create your views here.
#view python function must accept httprequest as object ,return httpresponse as object
def tasklist(request):
    if( 'username' in request.session):
        tasks=Task.objects.all()
        context={}
        context['tasks']=tasks
        return  render(request,'task/list.html',context)#HttpResponse('hi from task list view')
    else:
        return HttpResponseRedirect('/')

def taskadd(req):
    if ('username' in req.session):
        context={}
        context['catagories']=Catagory.objects.all()
        if(req.method=='POST'):
            cat=Catagory.objects.get(id=req.POST['catagory'])
            Task.objects.create(name=req.POST['taskname'],catagoryid=cat)
        return  render(req,'task/add.html',context) #HttpResponse('hi from add task view')
    else:
        return  HttpResponseRedirect('/')
def taskupdate(req,id):
    context={}
    context['catagories']=Catagory.objects.all
    context['taskdata']=Task.objects.get(id=id)
    if(req.method=='POST'):
        name=req.POST['taskname']
        Task.objects.filter(id=id).update(name=req.POST['taskname'],catagoryid=Catagory.objects.get(id=req.POST['catagory']) )
        return HttpResponseRedirect('/Tasks')

    return render(req,'task/update.html',context)

def taskDelete(request,ID):
    #delete from task-task where id=ID
    Task.objects.filter(id=ID).delete()
    return  HttpResponseRedirect('/Tasks')#HttpResponse('hi id ='+str(ID)+' deleted')