# Generated by Django 3.1 on 2020-09-09 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewApp', '0014_auto_20200907_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodaysSpecial',
            fields=[
                ('dish_id', models.AutoField(primary_key=True, serialize=False)),
                ('dname', models.CharField(default='', max_length=50)),
                ('dprice', models.IntegerField(default=0)),
            ],
        ),
    ]
