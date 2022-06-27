from django.shortcuts import render

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Directions, Doctors
from .serializers import DirectionSerializer, DoctorSerializer
from .pagination import DoctorsApiListPagination
from .filters import DoctorsFilter


class DirectionApiList(generics.ListAPIView):
    queryset = Directions.objects.all()
    serializer_class = DirectionSerializer


class DoctorApiList(generics.ListAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorsApiListPagination
    filterset_class = DoctorsFilter
    filter_backends = (DjangoFilterBackend,)
    

