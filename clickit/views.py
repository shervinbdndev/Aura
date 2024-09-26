from typing import Union

from django.contrib import messages
from django.urls.base import reverse
from django.views.generic.base import View
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

from utils.server_side_data import data

from account.models import UserCoinModel
from account.forms import RegisterForm, LoginForm





class MainView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        login_form: LoginForm = LoginForm()
        register_form: RegisterForm = RegisterForm()
        
        if (request.user.is_authenticated):
            return redirect(to=reverse('user-profile'))
        
        return render(
            request=request,
            template_name='click/index.html',
            context={
                'server': data,
                'login_form': login_form,
                'register_form': register_form,
            }
        )
        
        
        

class ClaimRewardView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        user_coin, created = UserCoinModel.objects.get_or_create(user=request.user)
        
        if (user_coin.has_claimed_reward):
            messages.error(
                request=request,
                message='You Already claimed the reward.',
            )
            
            return redirect(to=reverse('user-profile'))
        
        return render(
            request=request,
            template_name='click/reward.html',
            context={
                'server': data,
            },
        )
    
    def post(self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect]:
        user_coin, created = UserCoinModel.objects.get_or_create(user=request.user)
        
        if (user_coin.has_claimed_reward):
            messages.error(
                request=request,
                message='You Already claimed the reward.',
            )
            
            return redirect(to=reverse('user-profile'))
        
        user_coin.coins += data['reward']
        user_coin.has_claimed_reward = True
        user_coin.save()
        
        messages.success(
            request=request,
            message='Reward claimed successfully!',
        )
        
        return redirect(to=reverse('user-profile'))