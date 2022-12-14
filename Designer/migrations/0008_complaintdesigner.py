# Generated by Django 4.0.4 on 2022-06-20 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_newdeigner'),
        ('Designer', '0007_rename_feedback_feedbackdesigner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaintdesigner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=100)),
                ('attachment', models.ImageField(upload_to='uploads/complaintimages/')),
                ('vstatus', models.IntegerField(default=False)),
                ('replay', models.TextField(max_length=100)),
                ('doc', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.newuser')),
            ],
        ),
    ]
