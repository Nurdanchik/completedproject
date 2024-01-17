# Generated by Django 4.2.6 on 2024-01-16 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='media/nurbek.jpeg', upload_to='media/')),
                ('price_fund', models.DecimalField(decimal_places=2, max_digits=10)),
                ('whoisowner', models.TextField()),
                ('price_for_participating', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('time_for_registration_left', models.DateTimeField()),
            ],
        ),
    ]
