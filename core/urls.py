from django.contrib import admin
from django.urls import path, include 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.views import FacebookLogin, GithubLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')), 
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('auth/github/', GithubLogin.as_view(), name='github_login'),
]
