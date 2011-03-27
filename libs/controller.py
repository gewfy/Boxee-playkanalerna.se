import string
import mc
from urllib import quote
import playkanalerna

def categories():
	mc.ShowDialogWait()
	
	list = mc.ListItems()
	
	categories = playkanalerna.getCategories()
	for category in categories:
		item = mc.ListItem(mc.ListItem.MEDIA_UNKNOWN)
		item.SetLabel(str(category['name'].encode('utf-8','ignore')))
		item.SetPath(str(category['url'].encode('utf-8','ignore')))
		list.append(item)

	mc.ActivateWindow(14000)
	window = mc.GetWindow(14000)
	window.GetList(51).SetItems(list)
	
	mc.HideDialogWait()

def programs(url, category):
	mc.ShowDialogWait()

	list = mc.ListItems()

	programs = playkanalerna.getPrograms(url)
	for program in programs:
		item = mc.ListItem(mc.ListItem.MEDIA_UNKNOWN)
		item.SetLabel(str(program['name'].encode('utf-8','ignore')))
		item.SetPath(str(program['url'].encode('utf-8','ignore')))
		list.append(item)

	mc.ActivateWindow(14001)
	window = mc.GetWindow(14001)
	window.GetList(51).SetItems(list)
	window.GetLabel(30).SetLabel(category)
	
	mc.HideDialogWait()

def episodes(url, show):
	mc.ShowDialogWait()

	list = mc.ListItems()

	episodes = playkanalerna.getEpisodes(url)
	for episode in episodes:
		item = mc.ListItem(mc.ListItem.MEDIA_VIDEO_CLIP)
		item.SetLabel(str(episode['name'].encode('utf-8','ignore')))
		item.SetPath('flash://%s/src=%s&bx-jsactions=%s' % ("video", quote(str(episode['url'].encode('utf-8','ignore'))), quote('http://boxee.jakob.edge.vinnovera.se/tv3play.js')))
		if episode['image'] is not None:
			item.SetThumbnail(str(episode['image'].encode('utf-8','ignore')))
		list.append(item)

	mc.ActivateWindow(14002)
	window	= mc.GetWindow(14002)
	window.GetList(51).SetItems(list)
	window.GetLabel(30).SetLabel(show)
	
	mc.HideDialogWait()