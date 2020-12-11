from django.db import models


# Create your models here.
class Level1(models.Model):
    level1_choices = [('Asset', 'Assets'),
                      ('Equity', 'Equity'),
                      ('Liability', 'Liability'),
                      ('Revenue', 'Revenue'),
                      ('Expenses', 'Expenses'),
                      ]
    name = models.CharField(max_length=10, choices=level1_choices, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Level 1'


class Level2(models.Model):
    parent_level = models.ForeignKey(verbose_name="Level 1", to=Level1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Level 2'


class Level3(models.Model):
    parent_level1 = models.ForeignKey(verbose_name='Level 1', to=Level1, on_delete=models.CASCADE)
    parent_level = models.ForeignKey(verbose_name='Level 2', to=Level2, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.IntegerField()

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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Level 4'

class Level5(models.Model):
    parent = models.ForeignKey(to = Level4, on_delete=models.CASCADE)
    description = models.TextField(max_length=100, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    debit = models.IntegerField()
    
    def __str__(self):
        return f"{self.parent.code} - {self.parent.name}"

    class Meta:
        verbose_name_plural = 'Level 5'
