from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from chat.views.user import UserRegisterView, UserListView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register_user'),
    path('users/', UserListView.as_view(), name='user_list'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]