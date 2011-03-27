# -*- coding: utf-8 -*-
import sys
import string
import mc
import codecs
from elementsoup import ElementSoup

BASE_URL	= "http://www.playkanalerna.se"

HTTP = mc.Http()
HTTP.SetUserAgent("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)")

cache = {}

def getPageElements(url):
	print 'FETCHING: '+url
	if url in cache:
		print 'Cache found'
		page = cache[url]
	else:
		print 'No cache, fetching page'
		page = ElementSoup.parse(HTTP.Get(url))
		cache[url] = page

	return page
	
def getCategories():
	page		 		= getPageElements(BASE_URL)
	elements		= page.findall(".//ul[@class='categories']//a")
	categories	= []
	for item in elements:
		categories.append({
			'name':	item.text.strip(),
			'url':	BASE_URL+item.attrib['href']
		})
	return categories

def getLetters(url):
	page		 		= getPageElements(url)
	elements		= page.findall(".//section[@id='results']//span")
	letters			= []
	for item in elements:
		letters.append({
			'name': item.text.strip()
		})
	return letters
	

def getPrograms(url):
	page		 		= getPageElements(url)
	elements		= page.findall(".//section[@id='results']//li")
	programs		= []
	for item in elements:
		link = item.find('a')
		if link is not None:
			programs.append({
				'name': 		link.text.strip(),
				'channel':	item.attrib['class'].replace('p0', '').strip(),
				'url':			BASE_URL+link.attrib['href']
			})
	return programs
	
def getProgramInfo(url):
	page		 		= getPageElements(url)
	name				= page.find(".//div[@class='program-description-box']/h2")
	description	= page.find(".//div[@class='program-description-box']/div[@class='program-description']/p")
	info				= {
		'name':	name.text.strip()
	}
	
	if description is not None:
		info['description'] = description.text.strip()

	return info

def getEpisodes(url):
	page		 		= getPageElements(url)
	elements		= page.findall(".//div[@id='stream_list']//li/a")
	episodes		= []
	for item in elements:
		episode = {
			'name': 		item.find("span[@class='subtitle']").text.strip(),
			'url':			BASE_URL+item.attrib['href']
		}
		
		duration = item.find("span[@class='duration']")
		if duration is not None:
			episode['duration'] = duration.text.strip()
		
		image = item.find('.//img')
		if image is not None:
			episode['image'] = BASE_URL+image.attrib['src']
		else:
			episode['image'] = None

		episodes.append(episode)
	
	next = page.find(".//ul[@class='paginator']/li[@class='next']/a")
	if next is not None:
		episodes.extend(getEpisodes(BASE_URL+next.attrib['href'].encode('utf8')))
		
	return episodes
