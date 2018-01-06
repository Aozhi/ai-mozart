

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import randint
from django.shortcuts import render
from .forms import MusicForm
from .models import Music
# from utilities import pyprgm
from django.http import HttpResponseRedirect
import os

# Create your views here.

def index(request):
	return render(request, 'Website/index.html', {})

def play_it_happy(request):
	os.chdir("/home/saurabhbodhe/char-rnn")
	os.system("ls")
	num = randint(0, 5000)
	print ("Random generator: " + str(num))
	os.system("th shiz.lua -seed " + str(num) + " cv/lm_lstm_epoch50.00_0.9914.t7")
	os.system("ruby txt_to_midi.rb out.txt")
	os.system("cp output.mid /home/saurabhbodhe/Website/media/output.mid")
	os.chdir("/home/saurabhbodhe/ai-mozart")

	command = "timidity -T 70 media/output.mid -Ow -o outfile.mp3"
	os.system(command)

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def play_it_sad(request):
	os.chdir("/home/saurabhbodhe/char-rnn2")
	os.system("ls")
	num = randint(0, 5000)
	print ("Random generator: " + str(num))
	os.system("th shiz.lua -seed " + str(num) + " cv/lm_lstm_epoch20.07_0.6988.t7")
	os.system("ruby txt_to_midi.rb out.txt")
	os.system("cp output.mid /home/saurabhbodhe/Website/media/output.mid")
	os.chdir("/home/saurabhbodhe/Website")

	command = "timidity -T 30 media/output.mid -Ow -o outfile.mp3"
	os.system(command)

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def about(request):
	return render(request, 'Website/about.html', {})

def vf(request):
	return render(request, 'Website/vf.html', {})
