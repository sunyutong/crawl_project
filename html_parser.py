#!/usr/bin/python
import re
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

class HtmlParser(object):
	authors=[]

	re_get_name_pattern = '<span class="video-nickname" title="([\s\S]*?)">'
	re_get_num_pattern = '<span class="video-number">([\s\S]*?)</span>'

	def parser(self,html_cont,url):
		soup = bs(html_cont,"html.parser")
		items = soup.find_all('div',attrs={'class':'video-info'})
		return items

	def __refine_num(num):
		if '万' in num:
			num = float(num[0:-1])*10000
		else:
			num = int(num)
		return num

	def sorted(self,authors):
		authors = sorted(authors,key = HtmlParser.__sorted_seed,reverse = True)
		return authors

	def __sorted_seed(author):
		return HtmlParser.__refine_num(author['num'])

	def get_name_num(self,items):
		for i in items:
			name = i.find('span',attrs={'class':'video-nickname'}).get('title')
			num = i.find('span',attrs={'class':'video-number'}).get_text()
			author = {'name':name,'num':num}
			HtmlParser.authors.append(author)
		
		return HtmlParser.authors