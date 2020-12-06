from django.db import models
from datetime import timedelta, datetime, date
from django.utils import timezone
import calendar


def next_month():
    month = (date.today().month) % 12 + 1
    year = date.today().year
    day = 1
    return date(year, month, day)


# Create your models here.
class Designation(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Religion(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Religion'
        verbose_name_plural = 'Religions'


class Academic_Session(models.Model):
    YEAR_CHOICES = []
    for r in range(1980, (datetime.now().year + 10)):
        YEAR_CHOICES.append((r, r))

    start_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    end_year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year + 1)

    def __str__(self):
        return str(f"{self.start_year}-{self.end_year}")


class Class(models.Model):
    _class = models.CharField(max_length=10)
    academic_year = models.ForeignKey(Academic_Session, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self._class}({self.academic_year})"

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'


class Section(models.Model):
    section_name = models.CharField(max_length=10)

    def __str__(self):
        return self.section_name


class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class City(models.Model):
    name = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'



class Student(models.Model):
    date_of_admission = models.DateField()
    name = models.CharField(max_length=50)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    dob = models.DateField("Date of Birth")
    place_of_birth = models.ForeignKey(verbose_name="Place of Birth", to=City, on_delete=models.SET_NULL, null=True)
    cls = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='Class')
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    language_choice = (
        ('english', 'English'),
        ('urdu', 'Urdu'),
        ('other', 'Other'),
    )
    language = models.CharField(choices=language_choice, max_length=10, default='urdu')
    enrolled = models.BooleanField(default=False)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    cnic_b_form = models.BigIntegerField()
    pic = models.ImageField(upload_to='student_photo/', blank=True)
    guardian_contact_info = models.CharField(max_length=11, blank=False)
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Attendance(models.Model):
    attendance_date=models.DateField()
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Class : {self.class_id} , Date : {self.attendance_date}'


class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.attendance_id.attendance_date}/class:{self.attendance_id.class_id}/{self.student_id.name}'

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
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fee_month}-{self.fee_year}/{self.class_id._class}'

class FeeReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    fee_id=models.ForeignKey(Fee,on_delete=models.CASCADE)
    amount=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.fee_id.fee_month}-{self.fee_id.fee_year}/{self.student_id.name}'

