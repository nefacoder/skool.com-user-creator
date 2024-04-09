import requests
import json
import pandas as pd


def check_socks(host,port):
	try:
		r = requests.get("https://www.wikipedia.org", proxies=dict(http=f'socks5://{host}:{port}',
	                         https=f'socks5://{host}:{port}'), timeout=25)
		print('success')
		print(r.text)
		return 'success'
	except:
		print('fail')
		return 'fail'


res = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc')

out = json.loads(res.text)['data']
success = False
while success != True:
	for i in range(len(out)):
			host = out[i]['ip']
			port = out[i]['port']
			print(host)
			print(port)
			sock_out = check_socks(host, port)
			if sock_out == 'success':
				success = True
			else:
				success = False
		
