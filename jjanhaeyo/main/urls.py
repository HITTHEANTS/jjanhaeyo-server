"""jjanhaeyo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from accounts.views import accounts

admin.autodiscover()

schema_view = get_schema_view(
   openapi.Info(
      title='jjanhaeyo API',
      default_version='v1',
   ),
   public=False,
)

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    # path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/kakao/', accounts.KakaoLogin.as_view(), name='kakao_login'),
    path('rest-auth/facebook/', accounts.FacebookLogin.as_view(), name='facebook_login'),
    path('rest-auth/google/', accounts.GoogleLogin.as_view(), name='google_login'),
]

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
