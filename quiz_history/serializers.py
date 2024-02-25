from rest_framework import serializers
from . import models

class quiz_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.quiz_history
        fields = '__all__'
