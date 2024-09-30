from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serailzers import StudentSerailzer,UserSerailizer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# Create your views here.

@api_view(['POST'])
def register_user(request):
    serila = UserSerailizer(data = request.data)
    
    if not serila.is_valid():
        print(serila.errors)
        return Response({"status":403,"errors":serila.errors,"message":"something went wrong"})
    serila.save()
    
    user = User.objects.get(username = serila.data['username'])
    token_obj = Token.objects.get_or_create(user = user)

    return Response({"status":200,"payload":serila.data,"token" :str(token_obj), "message":"data saved"})


@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    student_serali = StudentSerailzer(student_obj,many=True)
    return Response({"status" : 200, "message": student_serali.data})

@api_view(['POST'])
def student_post(request):
    data = request.data
    serila = StudentSerailzer(data = request.data)

    if not serila.is_valid():
        print(serila.errors)
        return Response({"status":403,"errors":serila.errors,"message":"something went wrong"})
    serila.save()
    return Response({"status":200,"payload":serila.data,"message":"data saved"})

@api_view(['PUT'])
def student_put(request,id):
    try:
        studentobj = Student.objects.get(id = id)
        serila = StudentSerailzer(studentobj,data = request.data,partial = True)

        if not serila.is_valid():
            print(serila.errors)
            return Response({"status":403,"errors":serila.errors,"message":"something went wrong"})
        serila.save()
        return Response({"status":200,"payload":serila.data,"message":"data saved"})
    except Exception as e:
        print(e)
        return Response({"status":403,"message" : "Invalid id"})
    
@api_view(['DELETE'])
def delete_student(request,id):
    try:
        stud_obj = Student.objects.get(id = id)
        stud_obj.delete()
        return Response({"status":200,"Message":"user deleted"})
    except Exception as e:
        print(e)
        return Response({"status":403,"message" : "Invalid id"})