# Generated by Django 3.0 on 2020-12-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='account_no',
            new_name='account_no_1',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='account_no1',
            new_name='account_no_2',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='account_no2',
            new_name='account_no_3',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='bank_name',
        ),
        migrations.AddField(
            model_name='branch',
            name='bank_name_1',
            field=models.CharField(default='TEST', max_length=100),
        ),
        migrations.AddField(
            model_name='branch',
            name='bank_name_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='bank_name_3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]