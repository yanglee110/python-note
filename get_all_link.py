'''
获取一个初始链接中所有链接
'''

import urllib.request
import ssl
import re

def getlink(url):
    headers = ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url, context=ssl._create_unverified_context())
    data = str(file.read())

    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)

    link = list(set(link))
    return link

url = "https://shouji.jd.com/"
url2 = "http://blog.csdn.net"
linklist = getlink(url2)
print(linklist.__len__())
for link in linklist:
    print(link[0])
