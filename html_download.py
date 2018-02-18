#!/usr/bin/python
import urllib.request

class HtmlDownloader(object):
	
	def download(self,url):
		if url is None:
			return None
		else:
			response = urllib.request.urlopen(url)
			if response.getcode() != 200:
				return None
			else:
				return response.read()
