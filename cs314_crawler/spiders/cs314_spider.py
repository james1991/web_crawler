import scrapy
import logging
from cs314_crawler.items import Cs314CrawlerItem

class Cs314Spider(scrapy.Spider):
	name = "cs314"
	allowed_domains = ["utexas.edu"]
	start_urls = ["https://www.cs.utexas.edu/~scottm/cs314/"]

	def parse(self, response):
		for href in response.xpath('//a/@href').extract():
			url = response.urljoin(href)
			print url
			yield scrapy.Request(url, callback=self.parse_dir_contents)
		
	def parse_dir_contents(self, response):
	#def parse(self, response):

		#items = []
		#logger = logging.getLogger()

		for sel in response.xpath('//a'):
			item = Cs314CrawlerItem()
#  			temp = sel.xpath('@href').extract()[0]
			item['title'] = sel.xpath('text()').extract()
			item['link'] = sel.xpath('@href').extract()
			print item['link'][0]
			#logger.info(item['link'][0])
 			# if temp.startswith('www'):
#  				item['link'] = temp
#  			else:
#  				item['link'] = 'https://www.cs.utexas.edu/~scottm/cs314/' + temp
 			#items.append(item)
 		
 		#return items
 		
