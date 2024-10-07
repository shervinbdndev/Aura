# Generated by Django 5.1.1 on 2024-10-02 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upgrade', '0002_alter_cardupgrade_options_cardupgrade_card_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.AlterModelOptions(
            name='cardupgrade',
            options={'verbose_name': 'Card Upgrade', 'verbose_name_plural': 'Card Upgrades'},
        ),
        migrations.AddField(
            model_name='cardupgrade',
            name='to_card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='upgrade.card', verbose_name='Card'),
        ),
    ]
