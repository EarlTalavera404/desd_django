# Generated by Django 4.1.2 on 2023-01-10 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desd_assignment', '0010_alter_logmessage1_abc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logmessage1',
            name='abc',
        ),
    ]