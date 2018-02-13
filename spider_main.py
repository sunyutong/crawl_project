import html_download,html_parser

class Spider(object):

	def __init__(self):
		self.downloader = html_download.HtmlDownloader()
		self.parser = html_parser.HtmlParser()

	def crawl(self,root_url):
		html_cont = str(self.downloader.download(root_url),encoding = 'utf-8')
		result_html = self.parser.parser(html_cont,root_url)
		authors = self.parser.get_name_num(result_html)
		authors = self.parser.sorted(authors)
		self.parser.show(authors)

if __name__ == '__main__':
	root_url = "https://www.panda.tv/cate/hearthstone"
	spider = Spider()
	spider.crawl(root_url)
	