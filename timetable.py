#!/bin/python2
# coding=UTF-8

from bs4 import BeautifulSoup
import urllib

stops = {
	2: '台北站',
	3: '板橋站',
	4: '桃園站',
	5: '新竹站',
	6: '台中站',
	7: '嘉義站',
	8: '台南站',
	9: '左營站'
}

stops = {
	2: 'Taipei',
	3: 'Banqiao',
	4: 'Taoyuan',
	5: 'Hsinchu',
	6: 'Taichung',
	7: 'Chiayi',
	8: 'Tainan',
	9: 'Zuoying'
}

print u'train	direction	days	taipei	banqiao	taoyuan	hsinchu	taichung	chiayi	tainan	zuoying'

south_html = urllib.urlopen("http://www.thsrc.com.tw/tw/TimeTable/WeeklyTimeTable/1").read()
south = BeautifulSoup(south_html)
for row in south.find_all("tr"):
	cells = row.find_all("td")
	if len(cells) == 17:
		train = cells[1].contents[0]

		times = []
		for i in stops:
			times.append(unicode(cells[i].contents[0]))

		days = []
		for i, day in enumerate(cells[10:17]):
			if len(day.contents) == 0:
				days.append(str(i + 1))

		if len(days) > 0:
			print u'%s	south	%s	%s	%s	%s	%s	%s	%s	%s	%s' % (unicode(train), ",".join(days).rjust(13), times[0], times[1], times[2], times[3], times[4], times[5], times[6], times[7])

north_html = urllib.urlopen("http://www.thsrc.com.tw/tw/TimeTable/WeeklyTimeTable/0").read()
north = BeautifulSoup(north_html)
for row in north.find_all("tr"):
	cells = row.find_all("td")
	if len(cells) == 17:
		train = cells[1].contents[0]

		times = []
		for i in stops:
			times.append(unicode(cells[i].contents[0]))
		times.reverse()

		days = []
		for i, day in enumerate(cells[10:17]):
			if len(day.contents) == 0:
				days.append(str(i + 1))

		if len(days) > 0:
			print u'%s	north	%s	%s	%s	%s	%s	%s	%s	%s	%s' % (unicode(train), ",".join(days).rjust(13), times[0], times[1], times[2], times[3], times[4], times[5], times[6], times[7])

