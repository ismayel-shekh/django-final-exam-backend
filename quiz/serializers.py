from rest_framework import serializers
from . import models
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = '__all__'


class ChoiceSeritalizer(serializers.ModelSerializer):
    class Meta:
        model = models.Choice
        fields = '__all__'
        

class QuestionSeritalizer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = '__all__'





class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Review
        fields = '__all__'