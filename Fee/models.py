from datetime import datetime, date

from django.db import models


# Create your models here.
from Student.models import Class, Student


def next_month():
    month = date.today().month % 12 + 1
    year = date.today().year
    day = 1
    return date(year, month, day)


class Fee(models.Model):
    YEAR_CHOICES = []
    for r in range(2020, (datetime.now().year + 5)):
        YEAR_CHOICES.append((r, r))
    fee_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    Month_choices = [
        ('Jan', 'January'),
        ('Feb', 'February'),
        ('Mar', 'March'),
        ('Apr', 'April'),
        ('May', 'May'),
        ('Jun', 'June'),
        ('Jul', 'July'),
        ('Aug', 'August'),
        ('Sep', 'September'),
        ('Oct', 'October'),
        ('Nov', 'November'),
        ('Dec', 'December'),
    ]
    fee_month = models.CharField(choices=Month_choices, max_length=15, default='Jan')
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fee_month}-{self.fee_year}/{self.class_id.class_name}'


class FeeReport(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    fee_id = models.ForeignKey(Fee, on_delete=models.CASCADE)
    tuition_fee = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.fee_id.fee_month}-{self.fee_id.fee_year}/{self.student_id.name}'
