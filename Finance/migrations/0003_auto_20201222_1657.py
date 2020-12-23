# Generated by Django 3.0 on 2020-12-22 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Branch', '0003_auto_20201219_1420'),
        ('Finance', '0002_level1_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(unique_for_year=True)),
                ('end_date', models.DateField(unique_for_year=True)),
                ('is_active', models.BooleanField(default=False)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Branch.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField()),
                ('debit', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='level1',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='level2',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='level3',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='level4',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='level1',
            name='name',
            field=models.CharField(choices=[('Asset', 'Assets'), ('Liability', 'Liability'), ('Equity', 'Equity'), ('Revenue', 'Revenue'), ('Expenses', 'Expenses')], max_length=10, unique=True),
        ),
        migrations.DeleteModel(
            name='Level5',
        ),
        migrations.AddField(
            model_name='openingbalance',
            name='account_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Finance.Level4'),
        ),
        migrations.AddField(
            model_name='openingbalance',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Branch.Branch'),
        ),
        migrations.AddField(
            model_name='openingbalance',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Finance.FinancialYear'),
        ),
    ]