from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import *
from .form import *
from django.contrib.auth.models import *
from django.contrib.auth import login,authenticate,logout
from django.views.decorators.http import require_http_methods
#method get or post
@require_http_methods(['POST','GET'])
def RegistrationAdminModel(req):
    '''
    f=RegistrationAdminformModel()
    context={}
    context['form']=f
    if(req.method=='POST'):
        f=RegistrationAdminformModel(req.POST)
        if(f.is_bound and f.is_valid()):
            f.save()
    '''
    context={}
    User.objects.create_superuser(username='usersuper',email='user@gmail.com',password='123')
    return render(req,'RegistrationAdminModel.html',context)
# Create your views here.
def RegistrationAdmin(req):
    f=RegistrationAdminform()
    context={}
    context['form']=f
    if(req.method=='POST'):
        f=RegistrationAdminform(req.POST)
        if(f.is_bound and f.is_valid()):
            User.objects.create_superuser(username=req.POST['username'],password=req.POST['passworrd'],email=req.POST['email'])
            return HttpResponseRedirect('/admin')
    return render(req,'RegistrationAdmin.html',context)
def userlist(request):
    context={}
    for u in MyUser.objects.all():
        print(u.id,u.username)
    context['users']=MyUser.objects.all()
    context['user2']=MyUser.objects.filter(id=1)
    return  render(request,'listusers.html',context)
def Login(req):
    context={}
    if(req.method=='POST'):
        #xquery([obj1])
        u=MyUser.objects.filter(username=req.POST['email'],password=req.POST['password'])

        userobj=authenticate(username=req.POST['email'],password=req.POST['password'])
        print(userobj)
        if(len(u)!=0 and userobj is not  None):
            #add username in session
            req.session['username']=u[0].username
            login(req,userobj)
            return HttpResponseRedirect('/Tasks')
        else:
            context['msg']='invalid email or password'
    return render(req,'login.html',context=context)
    '''
    print('body',req.body)
    print('method',req.method)
    print('GET',req.GET)
    
    if(req.is_secure()):
        obj=HttpResponse('<h1>meta</h1>')
        obj.write('Django')
        obj['content-type']='text/plain'
        obj.set_cookie('Course','Django')
        #return HttpResponse('<h1>Login<h1></br>monifia branch')
        return obj
    else:
        return HttpResponse('not secure')
    '''
def Logout(req):
    logout(req)
    req.session.clear()
    return HttpResponse('Logout')

def Registration(req):
   context={}
   if(req.method=='POST'):
       username=req.POST['username']
       password=req.POST['password']
       email=req.POST['email']
       MyUser.objects.create(username=username,password=password,email=email,actiiv=1)
       '''
       u=MyUser(username=username)
       u.password=password
       u.email=email
       u.actiiv=1
       u.save()
       '''
   return  render(req,'register.html',context)