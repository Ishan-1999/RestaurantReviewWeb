# Generated by Django 3.1 on 2020-09-01 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewApp', '0005_auto_20200901_1406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='query',
            new_name='desc',
        ),
    ]
