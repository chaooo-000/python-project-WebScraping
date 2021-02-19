import urllib.request
import re
import os


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    return html


def get_page(html):
    p = r'<a href="https://www.gamersky.com/ent/202005/[^<]+>\d'
    page_list = re.findall(p, html)

    for each in range(len(page_list)):
        page_list[each] = page_list[each].split(">")[-1]
    return page_list


def get_img(folder, page_url):
    p = r'<a target="_blank" href="http://www.gamersky.com/showimage/id_gamersky.shtml\?([^"]+\.jpg)"'  # ?前的\很关键
    img_list = re.findall(p, page_url)

    for each in img_list:
        print(each)
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, f'G:\python project\Crawler\{folder}/{filename}')


if __name__ == '__main__':
    folder = 'pic'
    os.mkdir(f'G:\python project\Crawler\{folder}')  # 建文件夹
    os.chdir(f'G:\python project\Crawler\{folder}')  # 变路径
    url = 'https://www.gamersky.com/ent/202005/1289612.shtml'
    html = open_url(url)
    page_list = get_page(html)
    for i in page_list:
        if i != '1':
            page_url = f'https://www.gamersky.com/ent/202005/1289612_{i}.shtml'
        else:
            page_url = f'https://www.gamersky.com/ent/202005/1289612.shtml'
        html = open_url(page_url)
        get_img(folder, html)
