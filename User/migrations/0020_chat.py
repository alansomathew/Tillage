# Generated by Django 4.0.4 on 2022-07-01 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_newdeigner'),
        ('User', '0019_remove_complaintusertoshop_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('from_shop', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_shop', to='Guest.newshop')),
                ('from_user', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_user', to='Guest.newuser')),
                ('to_shop', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_shop', to='Guest.newuser')),
                ('to_user', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_user', to='Guest.newuser')),
            ],
        ),
    ]