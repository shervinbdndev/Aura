from django.http import Http404
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


from .models import CardUpgrade, Card

from account.models import UserCoinModel

from utils.server_side_data import data




class UpgradeCardsView(View):
    def get(self, request: HttpRequest, card_type: str) -> HttpResponse:
        user_coins, created = UserCoinModel.objects.get_or_create(user=request.user)
        
        cards = Card.objects.filter(card_type=card_type)
        user_upgrades = {upgrade.to_card.id: upgrade for upgrade in CardUpgrade.objects.filter(user=request.user)}

        return render(
            request=request,
            template_name='upgrade/upgrade.html',
            context={
                'card_data': [
                    {
                        'icon': card.icon,
                        'name': card.name,
                        'level': user_upgrades[card.id].card_level if card.id in user_upgrades else 1,
                        'cost': user_upgrades[card.id].card_upgrade_cost if card.id in user_upgrades else card.initial_upgrade_cost,
                        'description': card.description
                    }
                    for card in cards
                ],
                'coins': user_coins.coins,
                'has_claimed': user_coins.has_claimed_reward,
                'server': data,
            }
        )