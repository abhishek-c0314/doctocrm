# Generated by Django 3.2.23 on 2024-02-07 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRMAPP', '0016_rename_newleads_newlead'),
    ]

    operations = [
        migrations.DeleteModel(
            name='newlead',
        ),
    ]