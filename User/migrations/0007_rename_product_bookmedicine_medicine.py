# Generated by Django 4.0.4 on 2022-06-10 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_bookmedicine_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmedicine',
            old_name='product',
            new_name='medicine',
        ),
    ]