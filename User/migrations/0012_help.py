# Generated by Django 4.0.4 on 2022-06-20 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_newdeigner'),
        ('User', '0011_rename_feedback_feedbackuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='uploads/diseaseimages/')),
                ('discription', models.TextField(max_length=50)),
                ('title', models.TextField(max_length=15)),
                ('vstatus', models.IntegerField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.newuser')),
            ],
        ),
    ]
