

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import MusicForm
from .models import Music
# from utilities import pyprgm
from django.http import HttpResponseRedirect
import os

# Create your views here.

def index(request):
			# command = "timidity " + song.audio.url + " -Ow out.mp3"

	return render(request, 'Website/index.html', {})

def play_it(request):
	os.chdir("/home/mozart/char-rnn")
	print("i am here")
	os.system("ls")
	#os.system("cd 'char-rnn'")
	os.system("cp output.mid /home/mozart/Website/media/output.mid")
	os.system("th shiz.lua cv/lm_lstm_epoch33.77_0.7266.t7")
	os.system("ruby txt_to_midi.rb out.txt")
	


	#return render(request, 'Website/play_it.html', {})
	# return render(request, 'Website/play_it.html', {'urll': urll}
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
