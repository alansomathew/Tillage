# Generated by Django 4.0.4 on 2022-06-07 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_delete_newuser'),
        ('User', '0002_alter_newproduct_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='newproduct',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.category'),
        ),
    ]