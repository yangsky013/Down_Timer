# Generated by Django 3.2.5 on 2021-11-07 10:36

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('exercise_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('timer_name', models.CharField(max_length=255)),
                ('ready_min', models.IntegerField()),
                ('ready_sec', models.IntegerField()),
                ('exercise_min', models.IntegerField()),
                ('exercise_sec', models.IntegerField()),
                ('rest_min', models.IntegerField()),
                ('rest_sec', models.IntegerField()),
                ('round_count', models.IntegerField()),
                ('cycle_count', models.IntegerField()),
                ('between_cycle_min', models.IntegerField()),
                ('between_cycle_sec', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('is_active', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'timer',
            },
        ),
    ]
