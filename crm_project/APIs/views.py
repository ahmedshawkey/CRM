from django.shortcuts import render
from rest_framework import viewsets
from .models import Lead, Stage
from .serializers import LeadSerializer, StageSerializer

# Create your views here.


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
