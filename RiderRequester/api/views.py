from django.shortcuts import render
from rest_framework import viewsets
from api.models import Rider,Requester,Assets
from api.serializers import RiderSerializer,RequesterSerializer,AssetSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class RiderViewSet(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer

class RequesterViewSet(viewsets.ModelViewSet):
    queryset = Requester.objects.all()
    serializer_class = RequesterSerializer

    @action(detail=True,methods=['get'])
    def assets(Self, request,pk = None):
        try:
            id = Requester.objects.get(pk=pk)
            assets  = Assets.objects.filter(requester_id = id)
            asset_serializer = AssetSerializer(assets,many=True,context={'request':request})
            return Response(asset_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':"Requester does not exist"
            })


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all()
    serializer_class = AssetSerializer