from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from .services import *
from .serializers import *


class NetworkAPI(APIView):

    def get(self, request, **kwargs):
        adress = request.GET['q']
        city = adress.split(" ")[-1]
        infonet = NetworkOperatorCity.objects.select_related('city').select_related('operator').select_related('network').filter(city__name = city)
        infonet = NOCSerializer(infonet, many=True)
        return Response(infonet.data, status = 200)
