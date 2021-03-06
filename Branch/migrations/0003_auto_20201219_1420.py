# Generated by Django 3.0 on 2020-12-19 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0002_auto_20201219_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='bank_address_1',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='bank_address_2',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='bank_address_3',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='bank_contact_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='bank_contact_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='branch',
            name='bank_contact_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='bank_name_1',
            field=models.CharField(max_length=100),
        ),
    ]
