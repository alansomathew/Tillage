# Generated by Django 4.0.4 on 2022-06-07 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Designer', '0002_mname_stk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mname',
            name='stk',
        ),
    ]
