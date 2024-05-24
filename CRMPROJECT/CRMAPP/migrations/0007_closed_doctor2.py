# Generated by Django 3.2.23 on 2024-02-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMAPP', '0006_rename_tickets_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Closed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producttype', models.CharField(choices=[('select itiem', 'select item'), ('online', 'Online'), ('offline', 'Offline'), ('both', 'BOTH'), ('digital markecting + website', 'Digital Marketing + Website')], max_length=100)),
                ('product', models.CharField(choices=[('select product', 'Select product'), ('doctosmart corporate eye version', 'Doctosmart Corporate Eye version'), ('doctosmart basic plan', 'Doctosmart Basic Plan'), ('doctosmart corporate version', 'Doctosmart Corporate version'), ('doctosmart smart package', 'Doctosmart Smart Package'), ('software basic', 'Software Basic')], max_length=200)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('offer', models.CharField(choices=[('select offer', 'Select offer'), ('2 month free tab', '2 Month Free tab'), ('free tab', 'Free tab')], max_length=100)),
                ('installationdateandtime', models.DateTimeField()),
                ('durationfrom', models.DateTimeField()),
                ('durationto', models.DateTimeField()),
                ('installationtype', models.CharField(choices=[('online', 'Online'), ('on site', 'On Site')], max_length=60)),
                ('paymenttype', models.CharField(choices=[('select payament', 'Select Payment'), ('cash', 'Cash'), ('cheque', 'Cheque'), ('cod', 'COD'), ('upi', 'UPI')], max_length=100)),
                ('balance', models.IntegerField()),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=100)),
                ('name1', models.CharField(max_length=255)),
                ('phone1', models.CharField(max_length=15)),
                ('clinic1', models.CharField(max_length=255)),
                ('email1', models.EmailField(max_length=254)),
                ('specification1', models.CharField(max_length=50)),
                ('state1', models.CharField(max_length=50)),
                ('city1', models.CharField(max_length=50)),
                ('status1', models.CharField(max_length=100)),
            ],
        ),
    ]
