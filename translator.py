import urllib.request
import urllib.parse
import json

content = input('请输入要翻译的内容')
url = 'http://fanyi.youdao.com/translate'

data = {}   # 将自定义data转换成标准格式
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '15903052473803'
data['sign'] = '0e30d56e55c3249b1424afc5e2905c1c'
data['ts'] = '1590305247380'
data['bv'] = 'e453ce3cfeeb5745e100abbf212c590d'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTlME'

data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data)  # 发送用户请求
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400')
response = urllib.request.urlopen(req)           # 读取并解码内容
html = response.read()
target = json.loads(html)
print(target['translateResult'][0][0]['tgt'])
