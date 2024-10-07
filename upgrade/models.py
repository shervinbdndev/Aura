from django.db import models
from django.contrib.auth.models import User

from account.models import UserCoinModel



class Card(models.Model):
    TYPE_CHOICES: list[tuple[str, str]] = [
        ('manual', 'Manual'),
        ('advanced', 'Advanced'),
        ('business', 'Business'),
        ('legendary', 'Legendary'),
    ]
    
    card_type = models.CharField(max_length=10, choices=TYPE_CHOICES, blank=True, null=True, verbose_name='Type')
    name = models.CharField(max_length=100, blank=True, null=True ,verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    icon = models.CharField(max_length=100, blank=True, null=True ,verbose_name='Icon')
    initial_upgrade_cost = models.IntegerField(default=100, verbose_name='Upgrade Cost')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
    
    
    



class CardUpgrade(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='User')
    to_card = models.ForeignKey(to=Card, on_delete=models.CASCADE, default=1 ,verbose_name='Card')
    card_icon = models.CharField(max_length=100, blank=True, null=True ,verbose_name='Icon')
    card_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Name')
    card_level = models.PositiveIntegerField(default=1, verbose_name='Level')
    card_upgrade_cost = models.BigIntegerField(default=100, verbose_name='Upgrade Cost')
    card_description = models.TextField(max_length=150, verbose_name='Description')
    
    def __str__(self) -> str:
        return f'{self.user}/ Card => {self.card_name}/ Level => {self.card_level}'
    
    def upgrade(self):
        user_coins, created = UserCoinModel.objects.get_or_create(user=self.user)
        
        if (user_coins.coins >= self.card_upgrade_cost):
            user_coins.coins -= self.card_upgrade_cost
            
            self.card_level += 1
            self.card_upgrade_cost *= 2
            self.save()
            
            user_coins.save()
        
        else:
            raise ValueError('Not enough coins for upgrade.')
        
    
    class Meta:
        verbose_name = 'Card Upgrade'
        verbose_name_plural = 'Card Upgrades'