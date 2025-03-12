"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, viewsets, permissions
from rest_framework.authtoken.views import obtain_auth_token

from mysite.serializers.user_serializer import UserSerializer
from mysite.views.task_view import TaskViewSet
from mysite.serializers.user_serializer import UserSerializer
from mysite.views.change_password_view import ChangePasswordView
from mysite.views.generate_reset_code_view import GenerateResetCodeView
from mysite.views.journal_view import JournalViewSet
from mysite.views.mood_entry_view import MoodEntryViewSet
from mysite.views.survey_view import SurveyViewSet
from mysite.views.habit_view import HabitViewSet
from rest_framework.permissions import AllowAny



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'journals', JournalViewSet)
router.register(r'mood_entries', MoodEntryViewSet)
router.register(r'surveys',SurveyViewSet)
router.register(r'habits', HabitViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Momentum api",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.yourapi.com/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/login/', obtain_auth_token, name='auth'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='swagger-docs'),
    path('api/password-reset-code/', GenerateResetCodeView.as_view(), name='generate-reset-code'),
    path('api/reset-password/', ChangePasswordView.as_view(), name='reset-password'),

]







