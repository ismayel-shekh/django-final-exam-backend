from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer



class QuizViewSet(viewsets.ModelViewSet):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer

class availablequestionforspecificquestion(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view): # module user query_set
        question_id = request.query_params.get("question_id")
        if question_id:
            return queryset.filter(question = question_id)
        return queryset
class questionPagination(pagination.PageNumberPagination):
    page_size = 1
    page_query_param = 'page'
    max_page_size = 100
class QuestionViewset(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSeritalizer
    pagination_class = questionPagination
    filter_backends = [availablequestionforspecificquestion]

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Choice.objects.all()
    serializer_class = serializers.ChoiceSeritalizer

class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
