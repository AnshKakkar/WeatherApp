# Generated by Django 4.1.3 on 2022-12-19 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_Api', '0009_account_email_account_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
