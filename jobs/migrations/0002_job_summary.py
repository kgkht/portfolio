# Generated by Django 2.2.12 on 2020-05-21 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='summary',
            field=models.TextField(default=''),
        ),
    ]