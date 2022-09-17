# Generated by Django 4.0.4 on 2022-07-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0023_remove_chat_from_shop_remove_chat_to_shop_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmedicine',
            name='dstatus',
            field=models.IntegerField(default=False),
        ),
        migrations.AddField(
            model_name='bookproduct',
            name='dstatus',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='bookmedicine',
            name='delivering',
            field=models.CharField(default='Processing', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bookproduct',
            name='delivering',
            field=models.CharField(default='Processing', max_length=50, null=True),
        ),
    ]
