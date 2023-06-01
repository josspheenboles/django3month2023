from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .form import *
from django.views.generic import ListView,CreateView
# Create your views here.
class Catagoryadding(CreateView):
    model = Catagory
    template_name = 'catagory/add.html'
    fields='__all__'

    def form_valid(self, form):
        return  HttpResponseRedirect('/Catagory')

class Listcatagory(ListView):
    model = Catagory
class Addcatgaory(View):
    def get(self,request):
        context={}
        context['form']=CatagoryForm()
        return  render(request,'catagory/add.html',context)
    def post(self,request):
        f=CatagoryForm(request.POST)
        if(f.is_bound and f.is_valid()):
            f.save()
        return HttpResponse('<h1>post</h1>')
