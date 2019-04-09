#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:root
# datetime:19-3-14 下午3:04
# software: PyCharm

#//div[@class = "threadlist_title pull_left j_th_tit"]/a[@class = "j_th_tit"]/@href
#//img[@class = "BDE_Image"]/@src

import urllib
import urllib2
from lxml import etree

def loadPage(url,filename):
    print("正在下载" + filename)
    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    html = response.read()
    HTML_DOM_content = etree.HTML(html)
    link_list = HTML_DOM_content.xpath("//div[@class='t_con cleafix']/div/div/div/a/@href")
    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link
        print fulllink
        loadImage(fulllink)

def loadImage(link):
    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}
    request = urllib2.Request(link, headers = headers)
    response = urllib2.urlopen(request)
    html = response.read()
    HTML_DOM_content = etree.HTML(html)
    link_list = HTML_DOM_content.xpath('//img[@class = "BDE_Image"]/@src')
    for link in link_list:
        writeImage(link)
        print link


def writeImage(link):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}
    request = urllib2.Request(link, headers = headers)
    image = urllib2.urlopen(request).read()
    filename = link[-5:]
    d
    print "_" * 30

def tiebaSpider(url, beginPage, endPage, kw):
		"""
				作用:贴吧爬虫调度器，负责组合处理每个页面的url
				url:贴吧url的前部分
				beginPage:起始页
				endPage:结束页
		"""
		for page in range(beginPage, endPage + 1):
				pn = (page - 1) * 50
				filename = kw + "吧第" + str(page) + "页.html"
				fullurl = url + "&pn=" + str(pn)
				print fullurl
				html = loadPage(fullurl, filename)
				print html



if __name__ == '__main__':

		kw = raw_input("请输入需要爬取的贴吧名：")
		beginPage = int (raw_input("请输入起始页："))
		endPage = int (raw_input("请输入结束页："))

		url = "http://tieba.baidu.com/f?"
		key = urllib.urlencode({"kw":kw})
		print key
		fullurl  = url + key
		print fullurl
		tiebaSpider(fullurl, beginPage, endPage, kw)

