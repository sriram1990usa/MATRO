# Generated by Django 5.0.6 on 2024-07-08 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0004_auto_20220519_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytmhistory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]