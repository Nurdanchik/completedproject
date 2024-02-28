# Generated by Django 5.0.1 on 2024-02-28 05:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participating', '0001_initial'),
        ('tournaments', '0009_tournament_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cupon', models.CharField(max_length=20, unique=-1)),
                ('valid', models.BooleanField(default=True)),
                ('validuntil', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='cupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='participating.coupon'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament')),
            ],
        ),
    ]