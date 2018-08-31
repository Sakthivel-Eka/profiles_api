from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.

class HelloAPIView(APIView):
    def get(self,request,format=None):
        an_apiview=[
        'Uses HTTP methods as functions(GET,POST,PUT,PATCH,DELETE)',
        'Similar to traditional Django View',
        'Gives most control over our API logic',
        'Is Mapped manually to URLs',
        ]
        return Response({'message':'Hello!!','an_apiview': an_apiview})
