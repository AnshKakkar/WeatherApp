# Generated by Django 4.1.3 on 2022-12-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_Api', '0011_alter_account_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
