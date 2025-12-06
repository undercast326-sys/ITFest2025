from django.urls import path, include
from rest_framework.routers import DefaultRouter
from survey import views

router = DefaultRouter()
router.register('questions', views.QuestionViewSet)
router.register('choices', views.ChoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
