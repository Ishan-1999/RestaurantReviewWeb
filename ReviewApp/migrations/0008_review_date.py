# Generated by Django 3.1 on 2020-09-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewApp', '0007_auto_20200901_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.CharField(default='', max_length=50),
        ),
    ]
