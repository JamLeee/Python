from urllib.request import urlopen
import urllib.request
from bs4 import  BeautifulSoup
import os, time
import http.cookiejar
import  random 
from urllib.request import urlretrieve ,HTTPError ,urlopen,URLError
import re
import socks
import socket
import time

base_dir = './'
#下载图片
def download(url,file_name,index):
  dir =  base_dir+ 'mm' + '/'
  if not os.path.isdir(dir):
    os.makedirs(dir)
  file_name = file_name+str(index)
  dir = dir + file_name + '.jpg'
  try:
    with  urlopen(url,timeout=30) as r:
        content=r.read()
        with open(dir,'wb') as code:
            code.write(content)
    except:
    pass

#获取首页列表图库地址
def get_url_list(index,end):
  header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
  }
  url = 'http://www.27270.com/ent/meinvtupian/list_11_%s.html' % index
  req = urllib.request.Request(url,headers=header)
  r = urllib.request.urlopen(req)
  soup = BeautifulSoup(r,'html.parser',from_encoding='utf-8')
  girl_list = soup.select('body > div > div.MeinvTuPianBox > ul > li > a.MMPic')
  if not girl_list:
    print('已经全部抓取完毕')
  mm_href = []
  mm_names = []
  for mpoto in:
    mm_link = mpoto.get('href') 
    mm_nick = mpoto.get('title')
    mm_href.append(mm_link)
    mm_names.append(mm_nick)
  for gril,name in zip(mm_href,mm_names):
    print(gril+name)
    time.sleep(5)
    get_url_down(gril,name,end)
  index = index + 1
  #这是我的服务器的socks5的代理,你们可以换一下,也可以用html的做opener.
  if index % 2 == 0:
    socks.set_default_proxy(socks.SOCKS5, '192.168.30.102',1080)
    socket.socket = socks.socksocket
    get_url_list(index,end)
  else:
    get_url_list(index,end)
  #如果不用socks5,就直接
  #get_url_list(index,end)
  #如果是html的代理,可以生成opener来做.但是这样后面的urllib.request.urlopen(),就要改成opener.open了
  #这个就自行百度吧,我就不说了
  if index == end:
    os._exit(0)

def get_url_down(url,name,end):
  header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
  }
  req = urllib.request.Request(url,headers=header)
  r = urllib.request.urlopen(req)
  soup = BeautifulSoup(r,'html.parser',from_encoding='utf-8')
  soup_end = soup.select('body > div.warp.mar.oh > div.warp.oh > div.page-tag.oh > ul > li#pageinfo > a')
  end_down = re.findall(r"\d",str(soup_end))
  end1 = end_down[0]
  main_url = url
  index = 1
  list_index = 1
  mm_nick = photo_url(url)
  girl_down(mm_nick,name,list_index)
  for i in range(int(end1) - 1):
    if index <= int(end1):
        list_index = list_index + 1
        url2 = paging(main_url,list_index)
        print(url2)
        url_address=photo_url(url2)
        girl_down(url_address,name,list_index)
        index = index + 1
    else:
        break

#获取图片地址
def photo_url(url):
  header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
  }
  req = urllib.request.Request(url,headers=header)
  r = urllib.request.urlopen(req)
  soup = BeautifulSoup(r,'html.parser',from_encoding='utf-8')
  girl_list = soup.select('body > div.warp.mar.oh > div.warp.oh > div#picBody > p img')
  list_img = girl_list[0].get('src')
  print('图片地址:%s' %list_img)
  return list_img

#提交图片地址
def girl_down(url,name,index):
  download(url,name,index)

#下一页
def paging(url,index):
  str1 = url[:-5] + '_' + str(index) + url[-5:]
  return str1

if __name__ == '__main__':
  if not os.path.isdir(base_dir):
    os.makedirs(base_dir)
get_url_list(1,191)
