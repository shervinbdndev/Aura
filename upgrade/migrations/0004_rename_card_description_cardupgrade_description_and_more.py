# Generated by Django 5.1.1 on 2024-10-02 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upgrade', '0003_card_alter_cardupgrade_options_cardupgrade_to_card'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardupgrade',
            old_name='card_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='cardupgrade',
            old_name='card_icon',
            new_name='icon',
        ),
        migrations.RenameField(
            model_name='cardupgrade',
            old_name='card_level',
            new_name='level',
        ),
        migrations.RenameField(
            model_name='cardupgrade',
            old_name='card_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='cardupgrade',
            old_name='card_upgrade_cost',
            new_name='upgrade_cost',
        ),
    ]
