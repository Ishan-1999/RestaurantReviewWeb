# Generated by Django 3.1 on 2020-09-01 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewApp', '0006_auto_20200901_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='desc',
            new_name='review',
        ),
    ]
