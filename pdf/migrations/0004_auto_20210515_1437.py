# Generated by Django 3.1.5 on 2021-05-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0003_auto_20210424_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='construction_sum_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='construction_sum_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='construction_sum_4',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='construction_sum_5',
            field=models.CharField(default='', max_length=100),
        ),
    ]
