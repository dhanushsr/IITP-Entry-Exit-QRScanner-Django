# Generated by Django 2.1.3 on 2018-11-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entryexit', '0007_auto_20181110_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entryexit',
            name='entrytimestamp',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='entryexit',
            name='exittimestamp',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
