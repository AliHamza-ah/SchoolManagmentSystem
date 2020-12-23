from django import template
from django.db import models

# Create your models here.
from Branch.models import Branch

register = template.Library()


class Level1(models.Model):
    level1_choices = [('Asset', 'Assets'),
                      ('Liability', 'Liability'),
                      ('Equity', 'Equity'),
                      ('Revenue', 'Revenue'),
                      ('Expenses', 'Expenses'),
                      ]
    name = models.CharField(max_length=10, choices=level1_choices, unique=True)
    code = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Level 1'


class Level2(models.Model):
    parent_level = models.ForeignKey(verbose_name="Level 1", to=Level1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Level 2'


class Level3(models.Model):
    parent_level1 = models.ForeignKey(verbose_name='Level 1', to=Level1, on_delete=models.CASCADE)
    parent_level = models.ForeignKey(verbose_name='Level 2', to=Level2, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Level 3'


class Level4(models.Model):
    parent_level1 = models.ForeignKey(verbose_name='Level 1', to=Level1, on_delete=models.CASCADE)
    parent_level2 = models.ForeignKey(verbose_name='Level 2', to=Level2, on_delete=models.CASCADE)
    parent_level = models.ForeignKey(verbose_name='Level 3', to=Level3, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.BigIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} | {self.name}"

    class Meta:
        verbose_name_plural = 'Level 4'


class FinancialYear(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.end_date.year}"


class OpeningBalance(models.Model):
    year = models.ForeignKey(FinancialYear, on_delete=models.PROTECT)
    account_name = models.ForeignKey(Level4, on_delete=models.PROTECT)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    credit = models.IntegerField(default=None, null=True)
    debit = models.IntegerField(default=None, null=True)

    def __str__(self):
        return f"{self.year.end_date.year} | {self.account_name.name}"

