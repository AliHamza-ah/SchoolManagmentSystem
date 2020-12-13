# Generated by Django 3.0 on 2020-12-13 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.BigIntegerField()),
                ('landline', models.BigIntegerField()),
                ('address', models.TextField()),
                ('ntn', models.CharField(max_length=15)),
                ('bank_name', models.CharField(max_length=30)),
                ('account_no', models.BigIntegerField()),
                ('account_no1', models.BigIntegerField(blank=True)),
                ('account_no2', models.BigIntegerField(blank=True)),
                ('branch_manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
