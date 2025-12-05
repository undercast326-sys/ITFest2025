from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from webapp import views

router = DefaultRouter()
router.register('majors', views.MajorViewSet)
router.register('universities', views.UniversityViewSet)
router.register('types', views.TypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include(router.urls)),
    path('poll/', include('survey.urls'))
]
