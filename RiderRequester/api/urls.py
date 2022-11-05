from django.contrib import admin
from django.urls import path,include
from api.views import RiderViewSet,RequesterViewSet,AssetViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'riders', RiderViewSet)
router.register(r'requester', RequesterViewSet)
router.register(r'asset', AssetViewSet)
# router.register(r'Requester', Req)

urlpatterns = [ 
    path('',include(router.urls)) 
    
    ]
