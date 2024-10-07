# Generated by Django 5.1.1 on 2024-10-02 08:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CardUpgrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('card_level', models.PositiveIntegerField(default=1, verbose_name='Level')),
                ('card_upgrade_cost', models.BigIntegerField(default=100, verbose_name='Upgrade Cost')),
                ('card_description', models.TextField(max_length=150, verbose_name='Description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
