# Create your views here.
from main.models import *
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from scraper.skill_scraper import find_best_skills, get_url_list, get_personal_skills, find_related_courses
import requests
import json

def front_page(request):
	return render(request, 'frontpage.html', {})

def home_page(request):
	return render(request, 'homepage.html', {})

def symptoms_page(request):
	return render(request, 'symptomspage.html', {})

def submitJournalEntry(request):
	if request.method == 'POST':
		text = request.POST['entry']
		time = datetime.datetime.now()
		patientName = request.POST['patientName']
		journalEntry = models.DiaryEntry.objects.create(date=time, entry=text)
		journalEntry.save()

def makeNewUser(request):
	if request.method == 'POST':
		name = request.POST['name']
		DOB = request.POST['DOB']
		gender = request.POST['gender']
		newPatient = models.Patient.objects.create(name=name, doctor=,journal=)
		name = 