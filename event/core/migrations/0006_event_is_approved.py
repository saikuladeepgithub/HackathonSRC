# Generated by Django 5.0.6 on 2024-08-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
