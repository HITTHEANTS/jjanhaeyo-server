from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import verify_jwt_token

from accounts.views import accounts, devices
from accounts import views

router = DefaultRouter()
router.register('config', views.ConfigViewSet, basename='config')

urlpatterns = [
    path('users/me/', accounts.UserInfoView.as_view()),
    path('users/login/', accounts.UserLoginView.as_view()),
    path('users/register', accounts.UserRegisterView.as_view()),
    path('users/activate', accounts.UserActivateView.as_view()),
    path('token/refresh/', accounts.TokenRefreshView.as_view()),
    path('token/verify/', verify_jwt_token),
    path('devices/login/', devices.DeviceLoginView.as_view()),
    path('devices/register/', devices.DeviceRegisterView.as_view()),
    path('', include(router.urls)),
]
