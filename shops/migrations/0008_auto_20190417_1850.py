# Generated by Django 2.2 on 2019-04-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0007_auto_20190417_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]
