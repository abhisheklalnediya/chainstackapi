# Generated by Django 2.2 on 2019-04-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_user_quota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='quota',
            field=models.IntegerField(default=-1),
        ),
    ]