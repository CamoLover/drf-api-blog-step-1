from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from authentication.views import AuthorUserView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('users/', AuthorUserView.as_view(), name='user-list-create')
]