from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ResumeUploadView

urlpatterns = [
    path('resume/upload/', ResumeUploadView.as_view()),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


from .views import RegisterView
urlpatterns += [
    path('auth/register/', RegisterView.as_view(), name='register'),
]