# Generated by Django 4.1.2 on 2023-01-09 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desd_assignment', '0005_alter_logmessage1_repnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogMessage2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveBigIntegerField(default=2)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]

