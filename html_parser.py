#!/usr/bin/python
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class HtmlParser(object):
	authors=[]

	re_get_name_pattern = '<span class="video-nickname" title="([\s\S]*?)">'
	re_get_num_pattern = '<span class="video-number">([\s\S]*?)</span>'

	def parser(self,html_cont,url):
		re_pattern = '<div class="video-info">([\w\W]*?)</div>'
		root_html = re.findall(re_pattern,html_cont)
		return root_html

	def refine_num(num):
		if '万' in num:
			num = float(num[0:-1])*10000
		else:
			num = int(num)
		return num

	def sorted(self,authors):
		authors = sorted(authors,key = HtmlParser.sorted_seed,reverse = True)
		return authors

	def sorted_seed(author):
		return HtmlParser.refine_num(author['num'])

	def show(self,authors):
		for i in range(0,len(authors)):
			print('rank ' + str(i+1) + ':' + authors[i]['name'] +'------'+authors[i]['num'])


	def get_name_num(self,root_html):
		for l in root_html:
			name = re.findall(HtmlParser.re_get_name_pattern,l)[0]
			num = re.findall(HtmlParser.re_get_num_pattern,l)[0]

			author = {'name':name,'num':num}
			HtmlParser.authors.append(author)
		return HtmlParser.authors