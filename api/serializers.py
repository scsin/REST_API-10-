from rest_framework import serializers

from api.models import LambdaF

class ApiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LambdaF
        fields = ['lst']
