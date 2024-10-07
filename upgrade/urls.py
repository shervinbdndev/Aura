from django.urls import path

from . import views


urlpatterns = [
    path(
        route='<str:card_type>/',
        view=views.UpgradeCardsView.as_view(),
        name='upgrade-cards',
    ),
]