# Generated by Django 3.0 on 2020-12-18 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level1',
            name='code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
