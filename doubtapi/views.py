from django.shortcuts import render
from django.contrib import messages,auth
from django.shortcuts import get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser,FileUploadParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from .models import *
from .serializers import *
import json
from rest_framework.parsers import MultiPartParser,FormParser


# Create your views here.
def teacher(request):
    if request.method=='GET':
        doubts=Doubts.objects.all()
        serializers=DoubtSerializer(doubts,many=True)
        return JsonResponse(serializers.data,safe=False)
    

class student(APIView):
    parser_classes = (MultiPartParser, FormParser, )

    def post(self, request):
        serializer = DoubtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': "Teacher will get back to you soon :)"},status=201)
        return JsonResponse(serializer.errors,status=400)

        