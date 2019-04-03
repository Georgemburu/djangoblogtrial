from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import (
    CreateUser,
)

urlpatterns = [
    path('create/', CreateUser, name="create_user"),
    path('login/',LoginView.as_view(template_name = 'users/login.html'), name = 'user_login'),
    path('<int:pk>/logout/',LogoutView.as_view(template_name='users/logout.html'), name="user_logout")
]
