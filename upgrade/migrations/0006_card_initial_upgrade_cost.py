# Generated by Django 5.1.1 on 2024-10-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upgrade', '0005_rename_description_cardupgrade_card_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='initial_upgrade_cost',
            field=models.IntegerField(default=100, verbose_name='Upgrade Cost'),
        ),
    ]
