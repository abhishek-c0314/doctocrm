# Generated by Django 3.2.23 on 2024-02-06 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRMAPP', '0012_delete_closed'),
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
                ('cdt', models.DateTimeField(auto_now_add=True)),
                ('did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRMAPP.doctor2')),
            ],
        ),
    ]
