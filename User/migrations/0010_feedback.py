# Generated by Django 4.0.4 on 2022-06-18 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_newdeigner'),
        ('User', '0009_bookmedicine_delivering_bookproduct_delivering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.DateField(auto_now_add=True)),
                ('Feedback', models.TextField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.newuser')),
            ],
        ),
    ]
