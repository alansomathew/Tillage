# Generated by Django 4.0.4 on 2022-06-07 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_newdeigner'),
        ('TillageWizards', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Newproduct',
            new_name='NewMedicine',
        ),
    ]
