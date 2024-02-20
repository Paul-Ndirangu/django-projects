from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getFood(request):
    return  Response()

@api_view(['POST'])
def postFood(request):
    return Response()

