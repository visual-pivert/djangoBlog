# Generated by Django 4.1.5 on 2023-02-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_influenceur_alter_commentator_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='influenceur',
            name='date_joined',
            field=models.DateTimeField(auto_now=True, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='influenceur',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='influenceur',
            name='last_login',
            field=models.DateField(auto_now=True, verbose_name='last login'),
        ),
    ]