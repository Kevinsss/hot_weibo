# coding:utf-8

import json
import urllib2
import urllib
import datetime
import time
from bs4 import BeautifulSoup
from MailUtil import MailUtil

def work():
	# init
	headers = {
		'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
	}
	url = 'http://m.weibo.cn/container/getIndex?containerid=100803_-_page_hot_list'
	request = urllib2.Request(url, headers = headers)
	# get the weibo hot data
	try:
		data = urllib2.urlopen(request).read()
	except Exception, e:
		print str(e)
	if data is not None:
		data_analysis(data)
	else:
		print 'Network error, please try again!'

def data_analysis(data):
	sjson = json.loads(data)
	hotweibo_list = sjson['cards'][0]['card_group']
	text = ''
	for i in range(len(hotweibo_list)):
		text += str(i+1) + ". " + hotweibo_list[i]['card_type_name'] + '\n' + hotweibo_list[i]['desc1'] + '\n' + hotweibo_list[i]['desc2'] + '\n\n'
	sdate = datetime.datetime.now().strftime('%Y-%m-%d')
	
	# put your receiver address
	mail = MailUtil(['email address of receiver'], u'微博榜单' + sdate, text)
	# put your receiver address

	print 'Sending email.....'
	if mail.sendMail():
		print 'sucess!'
	else:
		print 'fail!'
if __name__ == '__main__':
	work()
