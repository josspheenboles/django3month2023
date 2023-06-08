# Create your views here.
from rest_framework.response import Response
from  rest_framework.decorators import  api_view
from .models import *
from .serliazers import *
from rest_framework.status import *
from django.shortcuts import  get_object_or_404
from rest_framework.permissions import  IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import permissions,authentication
from rest_framework.decorators import permission_classes
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteCatagory(req,id):
    data=get_object_or_404(Catagory,id=id)
    data.delete()
    return Response(status=HTTP_200_OK)

@api_view(['PUT'])

def UpdateCatagory(request,id):
    if(len(Catagory.objects.filter(id=id))!=0):
        updateobject=Catagory.objects.get(id=id)#cat1
        #catagory1ser.
        updateobjectafterupdate=Catagoryselizer(instance=updateobject,data=request.data)
        if(updateobjectafterupdate.is_valid()):
            updateobjectafterupdate.save()
            return Response(status=HTTP_202_ACCEPTED,data=updateobjectafterupdate.data)
    else:
        return  Response(status=HTTP_404_NOT_FOUND,data={'message':'id not found'})
@api_view(['POST'])
def AddCatagory(request):
    #Catagory.objects.create(name=request.data['name'])
    item=Catagoryselizer(data=request.data)
    if(item.is_valid()):
        item.save()
    return  Response(HTTP_200_OK)

@api_view(['GET'])
def overview(request):
    print(type(request))
    api_endpoint={
        'overview':'/',
        'AllCatagory':'/AllCatagory & get method',
        'AddCatagoty':'/AddCatagory & post method'
    }
    return  Response(api_endpoint)

@api_view(['GET'])
def ListCatagory(request,id=None):
    #select all catgory from model
    if(id is not None):
        data=Catagory.objects.get(id=id)
    else:
        data=Catagory.objects.all()

    if(data):
        if(id is not None):
            dataserlized=Catagoryselizer(data)
            return Response(status=HTTP_202_ACCEPTED, data={'data': dataserlized.data})
        else:
            dataserlized=Catagoryselizer(data,many=True)
            return Response(status=HTTP_207_MULTI_STATUS,data={'data':dataserlized.data       })
    else:
        return  Response(status=HTTP_404_NOT_FOUND)


@api_view(['GET'])
def GetCatagory(request,id):
    objcatgory=Catagory.objects.get(id=id)
    if(objcatgory is not None):
        return Response(data=Catagoryselizer(objcatgory).data)
    else:
        return  Response(status=HTTP_404_NOT_FOUND)