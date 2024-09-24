from django.urls import path

from . import views


urlpatterns = [
    path(
        route='profile/',
        view=views.UserProfileView.as_view(),
        name='user-profile',
    ),
    path(
        route='click/',
        view=views.UserIncrementCoinsView.as_view(),
        name='user-click',
    ),
    path(
        route='login/',
        view=views.UserLoginView.as_view(),
        name='user-login',
    ),
    path(
        route='register/',
        view=views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        route='logout/',
        view=views.UserLogoutView.as_view(),
        name='user-logout',
    ),
]