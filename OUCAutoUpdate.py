import requests
import time
import os

Loginkey = os.environ["LOGINKEY"]
Sendkey = os.environ["SENDKEY"]
form_data = os.environ["FORM_DATA"]


url = 'https://pingan.ouc.edu.cn/ncov/wap/default/save'

Cookies = {'eai-sess': Loginkey}

headers = {
	'Accept':'application/json, text/javascript, */*; q=0.01',
	'Referer':'https://pingan.ouc.edu.cn/ncov/wap/default/index',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
	'X-Requested-With':'XMLHttpRequest',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
	}

r = requests.post(url,data = form_data,headers = headers,cookies = Cookies)

fturl = 'https://sctapi.ftqq.com/' + Sendkey + '.send?title= '+time.strftime("%Y-%m-%d %X", time.localtime())+'&desp='+r.text

print(r.text)

requests.get(fturl)
