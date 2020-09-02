# Generated by Django 3.1 on 2020-09-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReviewApp', '0003_contact_ratings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('ratings', models.CharField(default='5', max_length=10)),
                ('query', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
