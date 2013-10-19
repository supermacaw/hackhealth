# Create your views here.
from main.models import *
import datetime
from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse, reverse_lazy
from django.core import serializers
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, date
from django import forms
import simplejson

#import models and forms here
from main.models import *
from main.forms import *


import re

def front_page(request):
    rc={}
    user = request.user
    if user.is_authenticated():
        return home_page(request)
    rc['rform'] = EmailRegisterForm()
    return render(request, "main/home/front_page.html", rc)



def signin(request):
    rc={}
    form = EmailRegisterForm()
    if request.method=="POST":
        form = EmailRegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['pw1']==form.cleaned_data['pw2'] and form.cleaned_data['pw1']:
                email=form.cleaned_data['email']
                boo = create_from_email_pwd(email=email, pwd=form.cleaned_data['pw1'], request=request)
                rc.update(boo['rc'])
                if not rc.get('error'):
                    return redirect('main.account_views.email_sent')
            else:
                rc['error']="Passwords don't match"
    rc['rform'] = form
    return render_to_response("main/home/home_page.html", rc, context_instance=RequestContext(request))



def signup(request):
    rc={}
    form = EmailRegisterForm()
    if request.method=="POST":
        form = EmailRegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['pw1']==form.cleaned_data['pw2'] and form.cleaned_data['pw1']:
                email=form.cleaned_data['email']
                boo = create_from_email_pwd(email=email, pwd=form.cleaned_data['pw1'], request=request)
                rc.update(boo['rc'])
                if not rc.get('error'):
                    return redirect('main.account_views.email_sent')
            else:
                rc['error']="Passwords don't match"
    rc['rform'] = form
    return render_to_response("main/home/home_page.html", rc, context_instance=RequestContext(request))



def about(request):

	return render(request, 'main/home/about.html', {})


def home_page(request):
	return render(request, 'main/home/home_page.html', {})

def symptoms_page(request):
	return render(request, 'main/home/symptoms_page.html', {})

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
		#newPatient = models.Patient.objects.create(name=name, doctor=,journal=)
