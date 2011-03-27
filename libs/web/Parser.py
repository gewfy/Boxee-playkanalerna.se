###################################
# ikbenjaap Boxee Framework 0.1.1 #
###################################
from elementsoup import ElementSoup
import HTTP


def GetElement(url, cacheTime=0):
		data = HTTP.Get(url, cacheTime)
		return ElementSoup.parse(data)
