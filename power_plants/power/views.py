from django.db.models import Avg, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.response import Response
from rest_framework.status import *


class PlantStates(ModelViewSet):
    serializer_class = GeneratorSerializer
    queryset = PowerGenerator.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['plant_state', 'plant_code']
    ordering_fields = ['annual_net_gen']

    def retrieve(self, request, pk=None):
        try:
            obj = PowerGenerator.objects.get(id=pk)
            count = PowerGenerator.objects.filter(plant_state=obj.plant_state).aggregate(Sum('annual_net_gen'))
            # count = PowerGenerator.objects.aggregate(Sum('annual_net_gen'))
            try:
                pr = obj.annual_net_gen / count['annual_net_gen__sum'] * 100
            except:
                pr = 0

            serializer = GeneratorSerializer(obj)
            data = serializer.data
            data['per'] = pr
            return Response(data, status=HTTP_200_OK)
        except:
            return Response({'msg': 'Invalid ID'}, status=HTTP_400_BAD_REQUEST)