# Generated by Django 2.2 on 2020-01-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('typing_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='accuracy',
            field=models.FloatField(),
        ),
    ]