# -*- coding: utf-8 -*-
##########################################
# SVTPlay by Jaap (jaaps on boxee forum) #
# See ikbenjaap.com for more apps        #
##########################################

import string
from web import Parser
from boxee import Dir
from urllib import quote

####################################################################
BASE_URL						= "http://www.playkanalerna.se"
MAIN_XPATH					= ".//section[@id='results']/ul/li/a"
EPISODE_XPATH				= ".//div[@id='stream_list']/div/div/ul/li/a"

MAIN_NEXT_XPATH				=	".//div[@id='am']//ul/li[@class='next ']/a/img"

EPISODE_NEXT_XPATH_IMG		= 	".//div[@id='sb']//ul/li[@class='next ']/a/img"
EPISODE_NEXT_XPATH_HREF		= 	".//div[@id='sb']//ul/li[@class='next ']/a[@href]"
####################################################################
subtitle = ""


def init():
	Dir.CreateDir()
	properties = {'subtitle': subtitle}
	element = Parser.GetElement(BASE_URL, 3600)
	for item in element.findall(MAIN_XPATH):
		properties = {'subtitle': subtitle}
		Dir.AddToDir(item.text.strip(), "", item.attrib["href"], "", properties)	
	Dir.PushDir()

def episodes(url):
	Dir.CreateDir(51, 14001)
	element = Parser.GetElement(BASE_URL+url, 3600)
	for item in element.findall(EPISODE_XPATH):
		properties = { 'title': item.find(".//*[@class='subtitle']").text.strip(), 'subtitle': subtitle }
		Dir.AddToDir(item.find(".//*[@class='subtitle']").text.strip(), item.find(".//*[@class='duration']").text.strip(),		'flash://%s/src=%s&bx-jsactions=%s' % ("svtplay", quote(BASE_URL+str(item.attrib["href"])), quote('http://boxee.ikbenjaap.com/svtplay.js')), 	item.find(".//img").attrib["src"], properties)
	Dir.PushDir()

# def shows(letter, page=1):
# 	if page == 1:	
# 		Dir.CreateDir(51, 14001)
# 	try:
# 		element = Parser.GetElement(BASE_URL+"/alfabetisk?am,"+str(letter)+","+str(page)+",thumbs", 3600)
# 		for item in element.findall(MAIN_XPATH):
# 			properties = {'subtitle': subtitle}
# 			Dir.AddToDir(	item.find(".//span").text.strip(),		item.find(".//a").attrib["title"].strip(),		item.find(".//a").attrib["href"].split("/")[2], 	item.find(".//img").attrib["src"], properties)
# 		
# 		try:
# 			if element.find(MAIN_NEXT_XPATH).attrib["src"] == "/img/button/pagination-next.gif":
# 				shows(letter, page+1)
# 		except:
# 			print "SVTPlay: Exception shows (2) (empty or only one page?)"
# 	except:
# 		print "SVTPlay: Exception shows (1) ()"
# 		
# 
# 	if page == 1:	
# 		Dir.PushDir()
		
# def episodes(id, page= ""):
# 	if page == "":	
# 		Dir.CreateDir(51, 14002)
# 	folder = 0
# 	try:
# 		if id.find("http://") != -1:
# 			element = Parser.GetElement(str(id)+"/"+str(page), 3600)
# 		else:
# 			element = Parser.GetElement(BASE_URL+"/t/"+str(id)+"/"+str(page), 3600)
# 		for item in element.findall(EPISODE_XPATH):
# 			try:
# 				if item.find(".//a").attrib["class"] == "folder overlay tooltip":
# 					if folder == 0:
# 						Dir.CreateDir(51, 14001)
# 						folder = 1
# 					properties = {'subtitle': subtitle}
# 					Dir.AddToDir(	item.find(".//span").text.strip(),		' ',		BASE_URL+"/t/"+str(id)+"/"+item.find(".//a").attrib["href"], 	item.find(".//img[@class]").attrib["src"], properties)
# 				else:
# 					properties = {'title' : item.find(".//span").text.strip(), 'subtitle': subtitle}
# 					if item.find(".//span").text.strip() != "":
# 						Dir.AddToDir(	subtitle + " - " + item.find(".//span").text.strip(),		item.find(".//em").text.strip(),		'flash://%s/src=%s&bx-jsactions=%s' % ("svtplay", quote(BASE_URL+str(item.find(".//a").attrib["href"])), quote('http://boxee.ikbenjaap.com/svtplay.js')), 	item.find(".//img").attrib["src"], properties)
# 			except:
# 				print "SVTPlay: Exception episodes (1) "
# 		if element.find(EPISODE_NEXT_XPATH_IMG).attrib["src"] == "/img/button/pagination-next.gif":
# 			if element.find(EPISODE_NEXT_XPATH_HREF).attrib["href"].split("/")[0] != page:
# 				episodes(id, element.find(EPISODE_NEXT_XPATH_HREF).attrib["href"])
# 	
# 	except:
# 		print "SVTPlay: Exception episodes (2)"
# 		
# 	if page == "":	
# 		Dir.PushDir()

		
def set_subtitle(label):
	global subtitle
	subtitle = label.decode('utf-8')