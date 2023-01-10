from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from .services import *
from .serializers import *


class NetworkAPI(APIView):

    def get(self, request, **kwargs):
    	adress = request.GET['q']
    	return Response(adress, status = 200)

"""
class ListAPI(APIView):

    def get(self, request, **kwargs):
    	listSociety = Society.objects.select_related('sector').all()
    	listSociety = SocietySerializer(listSociety, many=True)
    	return Response(listSociety.data, status = 200)

"""