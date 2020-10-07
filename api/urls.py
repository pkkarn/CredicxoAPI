from django.urls import path
from api import views

urlpatterns = [
    path('register/', views.resgisteration_view, name="register_api"),
]
