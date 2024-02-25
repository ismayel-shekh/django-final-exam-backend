from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()
# router.register('list')
router.register('category', views.CategoryViewSet)
router.register('quiz', views.QuizViewSet)
router.register('quetion', views.QuestionViewset)
router.register('choices', views.ChoiceViewSet)
router.register('reviews', views.ReviewViewset)

urlpatterns = [
    path('', include(router.urls))
]
