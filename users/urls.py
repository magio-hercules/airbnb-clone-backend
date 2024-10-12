from django.urls import path
from . import views

urlpatterns = [
    path("me", views.Me.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
    # 과제
    path("", views.Users.as_view()),
    path("<int:pk>", views.PublicUser.as_view()),
    path("<int:pk>/tweets", views.UserTweets.as_view()),
    path("password", views.ChangePassword.as_view()),
    path("login", views.LogIn.as_view()),
    path("logout", views.LogOut.as_view()),
]
