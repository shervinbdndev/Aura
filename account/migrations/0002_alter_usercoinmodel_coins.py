# Generated by Django 5.1.1 on 2024-09-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercoinmodel',
            name='coins',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Coins'),
        ),
    ]