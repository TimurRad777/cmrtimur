from django.shortcuts import render, redirect, reverse
from .models import Course, Teacher, Student, Transaction
from django.utils import timezone 
from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.core.paginator import Paginator

def index (request):
    return render (request, 'index.html')
    
