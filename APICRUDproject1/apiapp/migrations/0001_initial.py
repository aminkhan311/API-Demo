# Generated by Django 3.2.5 on 2021-07-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=20)),
                ('esal', models.FloatField()),
            ],
        ),
    ]
