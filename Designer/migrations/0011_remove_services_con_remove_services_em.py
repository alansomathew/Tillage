# Generated by Django 4.0.4 on 2022-06-22 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Designer', '0010_alter_complaintdesigner_attachment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='con',
        ),
        migrations.RemoveField(
            model_name='services',
            name='em',
        ),
    ]
