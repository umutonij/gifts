# Generated by Django 2.2 on 2019-04-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0010_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='choice',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='first_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='house_number',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='last_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='road_number',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='size',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
