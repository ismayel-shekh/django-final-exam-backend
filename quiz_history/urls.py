from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', views.quiz_historyViewset)
urlpatterns = [
    path('', include(router.urls))
]
