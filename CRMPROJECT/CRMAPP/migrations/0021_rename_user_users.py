# Generated by Django 3.2.24 on 2024-02-09 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRMAPP', '0020_logins_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='users',
        ),
    ]