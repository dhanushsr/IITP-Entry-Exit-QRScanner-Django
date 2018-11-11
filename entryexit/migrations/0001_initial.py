# Generated by Django 2.1.3 on 2018-11-09 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0004_auto_20181108_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EntryExit',
            fields=[
                ('entryno', models.IntegerField(primary_key=True, serialize=False)),
                ('entrytimestamp', models.DateTimeField(default=None)),
                ('exittimestamp', models.DateTimeField(default=None)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building_entries', to='entryexit.Building')),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='people.People')),
            ],
        ),
    ]