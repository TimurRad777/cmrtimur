from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Course(models.Model):
    status_choices= [
        ('не начатые', 'не начатые'),
        ('начатые', 'начатые'),
        ('архивные', 'архивные'),
    ]
    title=models.CharField("Название", max_length=100)
    date_start=models.DateTimeField("Дата публикации")
    date_end=models.DateTimeField("Дата публикации")
    status=models.CharField(choices=status_choices, max_length=255, default='не начатые')
    price=models.IntegerField("Стоимость")
    teacher=models.ForeignKey('Teacher', on_delete=models.PROTECT, verbose_name='Учитель', blank=True, null=True) 
    
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.title
    
class Teacher(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Учитель')
    phone_number=models.CharField("Номер телефона", max_length=17)
    birth_date=models.DateTimeField("День Рождения")
    description=models.TextField("Описание")
    percent=models.IntegerField("Проценты", default=0)
    
    
    def __str__(self):
        return self.user.username

class Transaction(models.Model):
    payment_type=[
    ('наличные', 'наличные'),
    ('безналичные', 'безналичные'),
    ]
    student=models.ForeignKey('Student', on_delete=models.PROTECT, blank=True, null=True)
    course=models.ForeignKey('Course', on_delete=models.PROTECT, blank=True, null=True)
    price=models.IntegerField("Стоимость")
    date=models.DateTimeField("Дата оплаты")
    description=models.TextField("Описание")
    payment_type=models.CharField(choices=payment_type, max_length=255, default='наличные')
    teacher=models.ForeignKey('Teacher', on_delete=models.PROTECT, verbose_name='Учитель', blank=True, null=True)
    
    def __str__(self):
        return self.student

class Student(models.Model):
    name=models.CharField("Имя", max_length=255)
    birth_date=models.DateTimeField("День Рождения")
    phone_number=models.CharField("Номер телефона", max_length=17)
    description=models.TextField("Описание")
    course=models.ManyToManyField('Course', verbose_name='Курсы')

    def __str__(self):
        return self.name