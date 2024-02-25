from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.quiz_historyViewset)
urlpatterns = [
    path('', include(router.urls))
]
