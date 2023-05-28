from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import *
# Create your views here.
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
        u=MyUser.objects.filter(email=req.POST['email'],password=req.POST['password'])
        if(len(u)!=0):
            #add username in session
            req.session['username']=u[0].username
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