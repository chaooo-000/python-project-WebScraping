# 何哲超 2020/7/15 目前只能够下载一页的图片
import urllib.request
import re
import os


def createFile(folder):
    if os.path.exists(f'G:\python project\Crawler\{folder}') is False:
        os.mkdir(f'G:\python project\Crawler\{folder}')  # 建文件夹
    os.chdir(f'G:\python project\Crawler\{folder}')  # 变路径


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    return html


def get_img(folder, html):
    p = r'<a href="([^"]+/)" class="">'
    url_list = re.findall(p, html)

    for each in url_list:
        html = open_url(each)
        p = r'title="点击查看下一张">[^<]+<img src="([^"]+\.jpg)"'
        pic = re.findall(p, html)
        for eachpic in pic:
            print(eachpic)
            filename = eachpic.split("/")[-1]
            urllib.request.urlretrieve(eachpic, f'G:\python project\Crawler\{folder}/{filename}')


if __name__ == '__main__':
    folderName = '新垣结衣'
    createFile(folderName)
    url = 'https://movie.douban.com/celebrity/1018562/photos/?type=C&amp;start=0&amp;sortby=like&amp;size=a&amp;subtype=a'
    html = open_url(url)
    get_img(folderName, html)
