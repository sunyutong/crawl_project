import html_download,html_parser,outputer

class Spider(object):

	def __init__(self):
		self.downloader = html_download.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = outputer.OutPuter()

	def crawl(self,root_url):
		#下载html页面
		html_cont = str(self.downloader.download(root_url),encoding = 'utf-8')

		#提取div信息
		result_html = self.parser.parser(html_cont,root_url)

		#获取主播信息，存入authors列表
		authors = self.parser.get_name_num(result_html)

		#对列表进行排序
		authors = self.parser.sorted(authors)

		#结果化输出
		self.outputer.show(authors)

if __name__ == '__main__':
	root_url = "https://www.panda.tv/cate/hearthstone"
	spider = Spider()
	spider.crawl(root_url)
	