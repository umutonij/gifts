# Generated by Django 2.2 on 2019-04-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='about_us',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='contact_info',
            new_name='closing_hours',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='days',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email_address',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='open_hours',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
