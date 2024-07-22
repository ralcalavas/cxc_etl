from django.db import models
from django.utils import timezone

class Agency(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'agency'


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    agency = models.ForeignKey(Agency, models.DO_NOTHING)
    profession = models.ForeignKey('Profession', models.DO_NOTHING)
    gender = models.ForeignKey('Gender', models.DO_NOTHING)
    ethnicity = models.ForeignKey('Ethnicity', models.DO_NOTHING)
    monthly_salary = models.DecimalField(max_digits=16, decimal_places=2)
    md5 = models.CharField(unique=True, max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'employee'


class Ethnicity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'ethnicity'


class Gender(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'gender'


class Profession(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'profession'
