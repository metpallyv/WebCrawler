# -*- coding: utf-8 -*-
import sys
import urllib
import urllib2
import re
import codecs
import urlparse
import time
from Queue import Queue, Empty as QueueEmpty

from bs4 import BeautifulSoup

def connectWeb(url):

	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	values = {'name':'Vardhaman', 'location':'Melrose', 'language':'Python'}
	headers = {'User-Agent': user_agent}
	data = urllib.urlencode(values)

	req = urllib2.Request(url,data,headers)
	try:
	   status = urllib2.urlopen(req)
	except urllib2.URLError as e:
		print e.reason
	UrlafterConnect = status.read()

	return UrlafterConnect

#Crawl and return t he list of webpages referenced in the links of the page for no keyphrase
def crawlWeb_no_keyword(UrlafterConnect):

	if not UrlafterConnect:
		print("Url is empty")
		return list() #return empty list
	#Get all the links
	soup = BeautifulSoup(UrlafterConnect)
	urllist = []

	for link in soup.find_all('a', href=True):
		crawl =  link.get('href')
		crawl_url = crawl.encode('utf-8')
		if not crawl_url:
			continue
		#links present in the same directory of /wiki, if so convert them to http form
		if crawl_url.startswith('/wiki'):
			if (crawl_url.find(':') == -1) and (crawl_url != "/wiki/Main_Page"):
				crawl_url = urlparse.urljoin("http://en.wikipedia.org",crawl_url)
				crawl_url, frag = urlparse.urldefrag(crawl_url)
				urllist.append(crawl_url)

		else:
			#Get only wiki links without colons in it and not redirecting to main page
			if crawl_url.startswith('http://en.wikipedia.org'):
				if crawl_url != "http://en.wikipedia.org/wiki/Main_Page":
					s = "http://en"
					crawl = crawl_url.lstrip("http://en")
					if crawl.find(':') == -1:
						crawl_url, frag = urlparse.urldefrag(crawl_url)
						urllist.append(crawl_url)
	#Remove duplicate entries from the list while returning
	return list(set(urllist))

def crawlWeb(UrlafterConnect,keyword):

	if not UrlafterConnect:
		print("Url is empty")
		return list()
	#Get all the links
	soup = BeautifulSoup(UrlafterConnect)
	urllist = []
	#check for the existence of keyword IR and crawl on those urls
	if re.search(keyword, str(soup), re.IGNORECASE) != None:
		for link in soup.find_all('a', href=True):
			crawl =  link.get('href')
			crawl_url = crawl.encode('utf-8')
			if not crawl_url:
				continue

		#links present in the same directory of /wiki, if so convert them to http form
			if crawl_url.startswith('/wiki'):
				if (crawl_url.find(':') == -1) and (crawl_url != "/wiki/Main_Page"):
					crawl_url = urlparse.urljoin("http://en.wikipedia.org",crawl_url)
					crawl_url, frag = urlparse.urldefrag(crawl_url)
					urllist.append(crawl_url)

			else:
			#Get only wiki links without colons in it and not redirecting to main page
				if crawl_url.startswith('http://en.wikipedia.org'):
					if crawl_url != "http://en.wikipedia.org/wiki/Main_Page":

						s = "http://en"
						crawl = crawl_url.lstrip("http://en")
						if crawl.find(':') == -1:

							crawl_url, frag = urlparse.urldefrag(crawl_url)
							urllist.append(crawl_url)
	#Remove duplicate entries from the list while returning
	return list(set(urllist))

def main(argv):
	argumen = len(sys.argv)
	url = sys.argv[1]
	crawled_urls = []
	url_queue = []
	UrlafterConnect = connectWeb(url)
	if argumen == 2:
		url_queue = crawlWeb_no_keyword(UrlafterConnect)

		f = open("./CrawledLinks_no_keyword.txt",'w')
		for link in url_queue:
			f.write(link.encode('utf-8'))
			f.write("\n")
		f.close()
	else:
		keyword = sys.argv[2]
		keyword = keyword.encode('utf-8')
		url_queue = crawlWeb(UrlafterConnect,keyword)
		#crawled_urls.extend(url_queue)
		count = 1

	#Since we need the depth as 3, crawl twice from the seed page
		while(count <=2):
			print count
			iter_list = []

			for link in url_queue:
				if crawled_urls.count(link) > 1:
				   # print "Duplicate URL, not crawling again"
					continue
				else:
					webpage = connectWeb(link)
					if not webpage:
						print "Couldn't fetch the webpage for link : "
						continue
					temp_list = crawlWeb(webpage,keyword)
					crawled_urls.append(link)

					iter_list.extend(temp_list)
			url_queue = list(iter_list)
			count = count + 1
			time.sleep(1)
		f = codecs.open("./CrawledLinks.txt","w","utf-8")
		for link in crawled_urls:
		f.write(link.decode('utf-8'))
			f.write("\n")
		f.close()

if __name__ == "__main__":
   main(sys.argv)
