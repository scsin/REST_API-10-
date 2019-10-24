from django.shortcuts import render
from rest_framework import (
    viewsets,
    mixins,
    generics,
    status
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import ApiModelSerializer
from api.models import LambdaF, api_lambdaf

class lambda_function(viewsets.ModelViewSet):
    queryset = LambdaF.objects.all()
    serializer_class = ApiModelSerializer

class ListAPIView(APIView):
    def get(self, request):
        serializer = ApiModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ApiModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return_data = sorted(request.data['question'], key=request.data['question'].count, reverse=True)
            # return Response({'solution': request.data}, status=status.HTTP_200_OK, content_type='application/json')
        return Response({'solution': return_data}, status=status.HTTP_200_OK)
