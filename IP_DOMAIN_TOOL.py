# -*- coding: utf-8 -*-
import re
import requests
import argparse

def argument():
    parser = argparse.ArgumentParser(prog='IP_DOMAIN', description='IP——域名整理小工具 by白泽Sec_ahui')
    parser.add_argument('-f','--file',help=u'指定要处理的文件名，例如：-f C:\test.txt',type=argparse.FileType('r+'))
    global args
    args = parser.parse_args()
argument()
if not args.file:
    print(u"请指定要处理的域名——IP文件，例如：-f C:\test.txt")
    exit()
IP_DOMAIN=args.file
ip=open('ip.txt','w+')
domain=open('domain.txt','w+')
lines=IP_DOMAIN.readlines()
lines=sorted(list(set(lines)))
c_dict={}
b_dict={}
for str in lines:
    if (re.match(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",str)):
        ip.write(str.strip()+'\n')
        c = re.findall('((?:\d*\.){2}(?:\d)*)',str.strip())
        if not c[0] in c_dict:
            c_dict[c[0]] = 1
        else:
            c_dict[c[0]] +=1
        b = re.findall('(^\d{0,3}.\d{0,3})',str.strip())
        if not b[0] in b_dict:
            b_dict[b[0]] = 1
        else:
            b_dict[b[0]] +=1
    if(".com" in str or ".cn" in str or ".net" in str or ".org" in str or ".top" in str or ".vip" in str or ".edu" in str):
        domain.write(str.strip()+'\n')
ip.write((u"您搜索的结果共包含{}个C段，统计结果如下：\n".format(len(c_dict))).encode("GBK","ignore"))
c_dict=sorted(dict.items(c_dict), key=lambda item:item[1], reverse=True)
for i,j in (c_dict):
    ip.write((U"C段：{}.0/24\t{}条数据在此C段中\n".format(i,j)).encode("GBK","ignore"))

b_dict=sorted(dict.items(b_dict), key=lambda item:item[1], reverse=True)
ip.write((u"您搜索的结果共包含{}个B段，统计结果如下：\n".format(len(b_dict))).encode("GBK","ignore"))
for i,j in (b_dict):
    ip.write((U"B段：{}.0/16\t{}条数据在此B段中\n".format(i,j)).encode("GBK","ignore"))
