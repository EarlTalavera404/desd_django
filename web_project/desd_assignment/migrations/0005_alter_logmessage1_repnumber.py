# Generated by Django 4.1.2 on 2023-01-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desd_assignment', '0004_alter_logmessage1_repnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmessage1',
            name='repNumber',
            field=models.PositiveIntegerField(default=2),
        ),
    ]