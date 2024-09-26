from typing import Union

from django.shortcuts import render
from django.urls.base import reverse
from django.shortcuts import redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.contrib.auth import logout, login, authenticate
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

from .models import UserCoinModel
from .forms import RegisterForm, LoginForm

from utils.rank import RankManager
from utils.server_side_data import data








class UserProfileView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        user_coins, created = UserCoinModel.objects.get_or_create(user=request.user)
        
        rank_manager: RankManager = RankManager()
        rank_manager.setUserRank(user=user_coins)
        
        return render(
            request=request,
            template_name='profile/profile.html',
            context={
                'coins': user_coins.coins,
                'has_claimed': user_coins.has_claimed_reward,
                'rank': rank_manager.user_rank,
                'xp_needed': rank_manager.user_exp_needed_for_next_rank,
                'server': data,
            },
        )
        
        
        
        





class UserIncrementCoinsView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        user_coins, created = UserCoinModel.objects.get_or_create(user=request.user)
        user_coins.coins += 1
        user_coins.save()
        
        rank_manager: RankManager = RankManager()
        rank_manager.setUserRank(user=user_coins)
        
        return JsonResponse({
            'coins': user_coins.coins, 
            'rank': rank_manager.user_rank,
            'xp_needed': rank_manager.user_exp_needed_for_next_rank,
        })










class UserLoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        login_form: LoginForm = LoginForm()
        
        return render(
            request=request,
            template_name='auth/signin.html',
            context={
                'server': data,
                'login_form': login_form,
            }
        )
    
    def post(self, request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        login_form: LoginForm = LoginForm(request.POST or None)
        
        if (login_form.is_valid()):
            cd = login_form.cleaned_data
            user = authenticate(
                request=request,
                username=cd['username'],
                password=cd['password'],
            )
            
            if (user is not None):
                login(
                    request=request,
                    user=user,
                )
                
                return redirect(to=reverse('user-profile'))
            
            else:
                login_form.add_error(
                    field='username',
                    error='No user found with the information given.',
                )
        
        return render(
            request=request,
            template_name='auth/signin.html',
            context={
                'server': data,
                'login_form': login_form,
            }
        )
    
    
    
    
    
    
    
    
    
class UserRegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        register_form: RegisterForm = RegisterForm()
        
        return render(
            request=request,
            template_name='auth/signup.html',
            context={
                'server': data,
                'register_form': register_form,
            }
        )
        
    def post(self, request: HttpRequest) -> Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]:
        register_form: RegisterForm = RegisterForm(request.POST or None)
        if (register_form.is_valid()):
            cd = register_form.cleaned_data
            if (cd['password'] != cd['con_password']):
                register_form.add_error(
                    field='password',
                    error='Passwords are not same as each other.',
                )
            elif (User.objects.filter(username=cd['username']).exists()):
                register_form.add_error(
                    field='username',
                    error='This username is already in use.',
                )
            else:
                user: User = User.objects.create_user(
                    username=cd['username'],
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    email=cd['email'],
                    password=cd['password'],
                    is_active=True,
                )
                
                login(
                    request=request,
                    user=user,
                )
                
                return redirect(to=reverse('reward'))
        
        else:
            register_form.add_error(
                field='password',
                error='Invalid credentials',
            )

        return render(
            request=request,
            template_name='auth/signup.html',
            context={
                'server': data,
                'register_form': register_form,
            }
        )









class UserLogoutView(View):
    def get(self, request: HttpRequest) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect]:
        logout(request)
        return redirect(to=reverse('index'))