# Generated by Django 5.0.2 on 2024-03-05 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_projectmodule_status_alter_status_status_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertask',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='usertask',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
