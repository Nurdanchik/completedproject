# Generated by Django 5.0.1 on 2024-03-02 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participating', '0003_alter_coupon_cupon_alter_request_cupon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='cupon',
            field=models.CharField(max_length=10),
        ),
    ]
