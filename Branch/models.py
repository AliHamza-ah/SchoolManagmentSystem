from django.db import models
from Student.models import City
from django.contrib.auth.models import User


# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=30, )
    email = models.EmailField()
    contact_no = models.BigIntegerField()
    landline = models.BigIntegerField()
    address = models.TextField()
    ntn = models.CharField(max_length=15)
    branch_manager = models.ForeignKey(User, on_delete=models.PROTECT)
    logo = models.ImageField(upload_to='media/Branch_logo/', blank=True, null=True)
    bank_name = models.CharField(max_length=30)
    account_no = models.BigIntegerField()
    account_no1 = models.BigIntegerField(blank=True, null=True)
    account_no2 = models.BigIntegerField(blank=True, null=True)


    def __str__(self):
        return f"{self.name}".capitalize()
