import urllib.request
import urllib.parse

url = {
	'http://fanyi.baidu.com/sug'
}

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}
data = {
	
}

request = urllib.request(url=url, headers=headers)
response = 