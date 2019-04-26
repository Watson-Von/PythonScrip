# coding:utf-8
import re
import urllib.request


def get_html(url):
    page = urllib.request.urlopen(url)
    html_code = page.read().decode('utf-8')
    return html_code


def get_image(html_code):
    # reg = r'<img src="(.+?\")"'
    reg = "<img[^>]+src\\s*=\\s*['\"]([^'\"]+)['\"][^>]*>"
    reg_img = re.compile(reg)
    img_list = reg_img.findall(html_code)
    x = 0
    for img in img_list:

        if str(img).find("http") == -1:
            continue

        urllib.request.urlretrieve(img, '%s.jpg' % x)
        x += 1
        print("下载的图片链接 : " + img)


print(u'-------网页图片抓取-------')
print(u'请输入url:')
url = input()
if url:
    pass
else:
    print(u'---没有地址输入正在使用默认地址---')
    # url = 'http://tieba.baidu.com/p/1753935195'
    url = 'https://blog.csdn.net/tzs_1041218129/article/details/52228905'
print(u'----------正在获取网页---------')
html_code = get_html(url)
print(u'----------正在下载图片---------')
get_image(html_code)
print(u'-----------下载成功-----------')
input('Press Enter to exit')
