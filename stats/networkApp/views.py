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
        infonet = getNetworkGroupedByOperators(infonet)
        #infonet = NOCSerializer(infonet, many=True)

        if(len(infonet) == 0):
            city = getCityFromPostCode(city)
            infonet = NetworkOperatorCity.objects.select_related('city').select_related('operator').select_related('network').filter(city__name = city)
            infonet = getNetworkGroupedByOperators(infonet)

        return Response(infonet, status = 200)
