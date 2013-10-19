from django.db import models
from django.contrib.auth.models import User
import urllib2, cStringIO, itertools
from django.core.files.base import ContentFile
from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import timezone
from datetime import datetime, date, timedelta
import random




class DiaryEntry(models.Model):
	date = models.DateTimeField()
	entry = models.TextField(blank=True)
	patient = models.ForeignKey(Patient)

class Doctor(User):
	patients = models.ManyToManyField(Patient, blank=True)

class UserInfo(Patient):
	email = models.EmailField(blank=False)
	age = models.IntegerField(blank=True, null=True)
	description = models.TextField(blank=True)

class Patient(User):
	name = models.TextField(blank = False)
	doctor = models.ManyToManyField(Doctor, blank=True)
	journal = models.ManyToManyField(DiaryEntry, blank=True)

class Disease(models.Model):
	name = models.TextField(blank = False)
	symptoms = models.ManyToManyField(Symptom, blank = True)

class Symptom(models.Model):
	name = models.TextField(blank = false)

