# Generated by Django 4.2.11 on 2024-05-03 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('sno', models.IntegerField(primary_key=True, serialize=False)),
                ('titel', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
            ],
        ),
    ]
