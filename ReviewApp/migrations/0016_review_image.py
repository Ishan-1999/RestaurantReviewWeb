# Generated by Django 3.1 on 2020-09-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewApp', '0015_todaysspecial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(default='', upload_to='ReviewApp/images'),
        ),
    ]