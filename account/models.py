from django.db import models
from django.contrib.auth.models import User






class UserCoinModel(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='User')
    coins = models.BigIntegerField(default=0, blank=True, verbose_name='Coins')
    has_claimed_reward = models.BooleanField(default=False, verbose_name='Claimed')
    
    def __str__(self) -> str:
        return f'{self.user}: {self.coins}'
    
    class Meta:
        verbose_name = 'User Coin'
        verbose_name_plural = 'Users Coins'