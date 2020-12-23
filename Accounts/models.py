from django.db import models
from django.contrib.auth.models import User, Group
from Branch.models import Branch


class Designation(models.Model):
    designation = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Designation'
        verbose_name_plural = 'Designations'

    def __str__(self):
        return self.designation


class Employee(models.Model):
    user = models.OneToOneField(User, related_name='employee', null=True ,  on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    designation = models.ForeignKey(Designation, null=True , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"
