# Generated by Django 4.0.4 on 2022-06-18 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_newdeigner'),
        ('User', '0010_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedback',
            new_name='Feedbackuser',
        ),
    ]