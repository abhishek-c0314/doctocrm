# Generated by Django 3.2.23 on 2024-02-03 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='newproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proname', models.CharField(max_length=50)),
                ('proprice', models.IntegerField()),
                ('protype', models.CharField(max_length=50)),
            ],
        ),
    ]