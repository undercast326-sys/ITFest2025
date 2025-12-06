from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from survey.views import survey
from webapp import views
from accounts.views import login, profile

router = DefaultRouter()
router.register('majors', views.MajorViewSet)
router.register('universities', views.UniversityViewSet)
router.register('types', views.TypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('poll/', include('survey.urls')),
    path('university/<int:pk>/', views.university_detail, name='university_detail'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('survey/', survey, name="survey")
]
