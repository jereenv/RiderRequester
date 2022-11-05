from rest_framework import serializers
from api.models import Rider,Requester,Assets


#create serializers here
class RiderSerializer(serializers.HyperlinkedModelSerializer):
    rider_id=serializers.ReadOnlyField()
    class Meta:
        model=Rider
        fields="__all__"
        
        
        
class RequesterSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()    
    class Meta:
        model=Requester
        fields="__all__"


class AssetSerializer(serializers.HyperlinkedModelSerializer):   
    class Meta:
        model=Assets
        fields="__all__"