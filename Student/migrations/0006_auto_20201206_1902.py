# Generated by Django 3.0 on 2020-12-06 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_fee_feereport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='_class',
            new_name='class_name',
        ),
    ]