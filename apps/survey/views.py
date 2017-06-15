# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    print "index"
    request.session['counter'] = 0
    return render(request, 'survey/index.html')

def process(request):
    print "process"
    if  request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        print request.session
        request.session['counter'] += 1
    else:
        print "not post"
        return redirect ('/')
    return redirect('/results')

def results(request):
    print "results"
    return render(request, 'survey/results.html')
# Create your views here.
