# Generated by Django 2.2 on 2019-04-17 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0006_auto_20190417_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
