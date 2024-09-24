from django.urls import path
from . import views



urlpatterns = [
    path(
        route='',
        view=views.MainView.as_view(),
        name='index',
    ),
    path(
        route='reward/',
        view=views.ClaimRewardView.as_view(),
        name='reward',
    ),
]