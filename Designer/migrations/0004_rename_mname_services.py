# Generated by Django 4.0.4 on 2022-06-07 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_newdeigner'),
        ('Designer', '0003_remove_mname_stk'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mname',
            new_name='Services',
        ),
    ]