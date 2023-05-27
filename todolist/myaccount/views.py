from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def Login(req):
    return render(req,'login.html')
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

    return HttpResponse('Logout')

def Registration(req):
   '''
    print(req)
    #return HttpResponse('Registration')
    obj=JsonResponse({'course':'django'})
    return  obj
   '''
   context={}
   context['title']='To Do List'
   context['user']='normal'
   return  render(req,'register.html',context)