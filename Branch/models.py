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
    logo = models.ImageField(upload_to='media/Branch_logo/', blank=True, null=True)
    bank_name_1 = models.CharField(max_length=100)
    account_no_1 = models.BigIntegerField()
    bank_address_1 = models.CharField(max_length=300, null=True, blank=True)
    bank_contact_1 = models.IntegerField(null=True, blank=True)
    bank_name_2 = models.CharField(max_length=100, null=True, blank=True)
    account_no_2 = models.BigIntegerField(blank=True, null=True)
    bank_address_2 = models.CharField(max_length=300, null=True, blank=True)
    bank_contact_2 = models.IntegerField(null=True, blank=True)

    bank_name_3 = models.CharField(max_length=100, null=True, blank=True)
    account_no_3 = models.BigIntegerField(blank=True, null=True)
    bank_address_3 = models.CharField(max_length=300, null=True)
    bank_contact_3 = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}".capitalize()

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
