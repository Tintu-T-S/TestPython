# Generated by Django 4.2.1 on 2023-07-06 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_remove_players_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='date',
            field=models.DateField(default='1989-06-07'),
            preserve_default=False,
        ),
    ]
