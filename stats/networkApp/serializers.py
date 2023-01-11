from rest_framework import serializers
from .models import NetworkOperatorCity


class NOCSerializer(serializers.ModelSerializer):
	class Meta:
		model = NetworkOperatorCity
		depth = 1
		fields = (
			'id',
			'city',
			'network',
			'operator', 
			)
