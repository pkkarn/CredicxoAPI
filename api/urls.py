from django.urls import path
from api import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', views.resgisteration_view, name="register_api"),
    path('admin/', views.AdminView.as_view(), name="hello"),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name="access_token"),  # For Access Token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name="refresh_token"),  # For Access Token
]
