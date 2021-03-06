from django.urls import path, include
from api import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', views.resgisteration_view, name="register_api"),
    path('admin/', views.admin_view, name="admin"),
    path('student/', views.student_view, name="student"),
    path('teacher/', views.teacher_view, name="teacher"),
    path('admin/<int:pk>/', views.admin_update_view, name="admin_update"),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name="access_token"),  # For Access Token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name="refresh_token"),  # For Access Token
]
