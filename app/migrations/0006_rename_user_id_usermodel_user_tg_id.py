# Generated by Django 5.1.6 on 2025-03-04 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_bookingmodel_session_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='user_id',
            new_name='user_tg_id',
        ),
    ]
