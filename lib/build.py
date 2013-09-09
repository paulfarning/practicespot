#!/usr/bin/python

# Requires https://github.com/Ciantic/mpeg1audio/
import mpeg1audio
import os
import datetime
from fnmatch import fnmatch

dir = 'audio' # Directory to generate from
title = 'Practicespot' # Page title
html = open('lib/html/template.html').read() # Location of html template
pattern = '*.mp3' # Match mp3 files only
listing = ''
allTimes = [] # List to hold all timedeltas for page total time
wrap = 0

# Return 's' if number is greater than 1
def isPlural(number):
	return '' if number == 1 else 's'

# Convert timedelta object to English words
def timeToWords(tdelta):
	words = ''
	seconds = tdelta.seconds

	days = seconds / 86400
	seconds -= days * 86400

	hours = seconds / 3600
	seconds -= hours * 3600

	minutes = seconds / 60
	seconds -= minutes * 60

	if days:
		words += str(days) + ' day' + isPlural(days) + ', '
	if hours:
		words += str(hours) + ' hour' + isPlural(hours) + ', '
	if minutes:
		words += str(minutes) + ' minute' + isPlural(minutes) + ' and '
	if seconds:
		words += str(seconds) + ' second' + isPlural(seconds) + ' of your life'

	return words


for top, dirs, files in os.walk(dir):
	# Designed for directories named by date in format YYMMDD,
	# sort newest to oldest
	dirs.sort(reverse=True)
	if top == dir:
		# Save total to determine is end later
		total = len(dirs)
	else:
		if wrap % 3 == 0:
			listing += '<div class="row">'

		dirname  = top.replace(dir + os.sep, '')
		listing += '<div><h2>' + dirname + '</h2>'

		listing += '<ol>'
		sessionTimes = [] # Save all the session timedeltas to sum later
		for (counter, name) in enumerate(files):
			if fnmatch(name, pattern):
				try:
					mp3 = mpeg1audio.MPEGAudio(open(os.path.join(top, name), 'rb'))
				except mpeg1audio.MPEGAudioHeaderException:
					pass
				else:
					if counter == len(files) - 1:
						listing += '<li class="last">'
					else:
						listing += '<li>'
					listing += '<a href="' + os.path.join(top, name) + '">'
					listing += name.replace('.mp3', '') + '</a>'
					listing += '<span>' + str(mp3.duration) + '</span></li>'
					sessionTimes.append(mp3.duration)
					allTimes.append(mp3.duration)
		listing += '<li class="last zip"><a href="' + os.path.join(top, dirname) +'.zip">' + dirname + '.zip</a>'
		listing += '<span>' + str(sum(sessionTimes, datetime.timedelta())) + '</span></li>'
		listing += '</ol></div>'
		if wrap % 3 == 2 or wrap == total - 1:
			listing += '</div>'

		wrap += 1

# Swap content into template placeholders
html = html.replace('{{ $title }}', title)
html = html.replace('{{ $duration }}', timeToWords(sum(allTimes, datetime.timedelta())))
html = html.replace('{{ $listing }}', listing)

open("index.html", "w").write(html)
