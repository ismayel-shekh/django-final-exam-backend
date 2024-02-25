from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class quiz_historyViewset(viewsets.ModelViewSet):
    queryset = models.quiz_history.objects.all()
    serializer_class = serializers.quiz_historySerializer

    def get_queryset(self):
        queryset= super().get_queryset()
        participator_id = self.request.query_params.get('participator_id')
        if participator_id:
            queryset = queryset.filter(participator_id = participator_id)
        return queryset